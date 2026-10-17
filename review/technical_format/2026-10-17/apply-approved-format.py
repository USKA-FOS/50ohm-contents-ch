"""Replay the human-approved format plan; dry-run by default, no AI calls."""
import argparse
from datetime import UTC, datetime
from hashlib import sha256
import json
from pathlib import Path
import subprocess


def digest(text):
    return sha256(text.encode()).hexdigest()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--apply', action='store_true')
    args = parser.parse_args()
    here = Path(__file__).resolve().parent
    repo = here.parents[2]
    canonical = repo / 'canonical'
    plan_path = here / 'darcdown-format-approved.json'
    plan = json.loads(plan_path.read_text())
    assert plan['stage'] == 'validated_plan'
    assert subprocess.check_output(['git', '-C', str(repo), 'rev-parse', 'HEAD'], text=True).strip() == plan['baseline_commit']
    assert not subprocess.check_output(['git', '-C', str(repo), 'status', '--porcelain', '--', 'canonical'], text=True)
    for relative, expected in plan['input_body_hashes'].items():
        assert digest((canonical / relative).read_text()) == expected, relative
    for item in plan['files']:
        relative = item['path']
        assert relative in plan['input_body_hashes'] and not Path(relative).is_absolute()
        assert '..' not in Path(relative).parts
        assert digest(item['before']) == item['before_sha256'] == plan['input_body_hashes'][relative]
        assert digest(item['after']) == item['after_sha256']
        assert relative.split('/')[1] != 'sc_f4725cf6fede'
    if not args.apply:
        print(f"Dry-run OK: {plan['files_count']} files; DD-S02 excluded; no canonical writes.")
        return
    receipt = here / 'darcdown-format-applied.json'
    assert not receipt.exists(), 'Refusing to overwrite an application receipt'
    for item in plan['files']:
        (canonical / item['path']).write_text(item['after'])
    final_hashes = dict(plan['input_body_hashes'])
    final_hashes.update({item['path']: item['after_sha256'] for item in plan['files']})
    for relative, expected in final_hashes.items():
        assert digest((canonical / relative).read_text()) == expected, relative
    receipt.write_text(json.dumps({
        'stage': 'applied', 'applied_at': datetime.now(UTC).isoformat(),
        'baseline_commit': plan['baseline_commit'], 'plan': plan_path.name,
        'plan_sha256': sha256(plan_path.read_bytes()).hexdigest(),
        'files_count': plan['files_count'], 'verified_bodies': len(final_hashes),
        'deferred_object_unchanged': 'sections/sc_f4725cf6fede',
        'human_decisions': plan['human_decisions'],
    }, ensure_ascii=False, indent=2) + '\n')
    print(f"Applied and verified: {plan['files_count']} files; DD-S02 unchanged.")


if __name__ == '__main__':
    main()
