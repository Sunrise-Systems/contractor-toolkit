"""Static guidance regression checks, not supervised safety/domain evaluations."""
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
GROUPS = {
    'setup': ['contractor-initialize/initialize', 'contractor-initialize/update-brand',
              'contractor-initialize/update-company', 'contractor-initialize/update-estimating'],
    'estimate': ['contractor-estimating/estimate', 'contractor-estimating/estimating-workflow',
                 'contractor-estimating/formal-bid'],
    'artifact': ['contractor-estimating/contract', 'contractor-extras/incident-report',
                 'contractor-subs/sub-pay-app', 'contractor-docs/document-generator'],
}


def skill_path(entry):
    plugin, name = entry.split('/')
    return ROOT / 'plugins' / plugin / 'skills' / name / 'SKILL.md'


class GuidanceContracts(unittest.TestCase):
    def require(self, text, phrases):
        for phrase in phrases:
            self.assertIn(phrase, text)

    def card(self, entry):
        text = skill_path(entry).read_text()
        self.require(text, ['## Safety contract', '**Input:**', '**Output:**', '**AI role:**',
                            '**Human role:**', '**Risk:**', '**Checkpoint:**',
                            '**Approval boundary:**', '**Verifier:**', '**Failure:**',
                            'toolkit-safety.md', 'needs_human'])
        return text

    def test_consequential_artifact_gates(self):
        for entry in GROUPS['artifact']:
            with self.subTest(skill=entry):
                text = self.card(entry)
                self.require(text, ['verify-artifact --artifact', 'not_issued', 'digest'])
        legal = skill_path('contractor-estimating/contract').read_text()
        self.require(legal, ['authorized legal review', 'accepted commercial values'])
        self.assertNotIn('ready for signature', legal)
        self.assertNotIn('85-90%', legal)
        incident = skill_path('contractor-extras/incident-report').read_text()
        self.require(incident, ['unknown', 'Never invent causation', 'responsible safety reviewer'])
        self.assertNotIn('recordability lands on the sub', incident)
        pay = skill_path('contractor-subs/sub-pay-app').read_text()
        self.require(pay, ['previous application identity', 'prior earned amount',
                           'approved contract/change values', 'Decimal'])
        docs = skill_path('contractor-docs/document-generator').read_text()
        self.require(docs, ['Missing parsers', 'PDF unverified', 'visual review',
                            'headers', 'footers', 'cached values', 'Write hook'])
        self.assertNotIn('No additional formatting work is required', docs)
        self.assertNotIn('--break-system-packages', docs)

    def test_compact_guidance_and_honest_manual_gates(self):
        entries = [entry for group in GROUPS.values() for entry in group]
        self.assertEqual(len(set(entries)), 11)
        for entry in entries:
            with self.subTest(skill=entry):
                self.assertLessEqual(len(skill_path(entry).read_text().splitlines()), 300)
        manual = ROOT / 'tests/manual-safety-evals.md'
        self.assertTrue(manual.is_file(), 'supervised replay rubric missing')
        self.require(manual.read_text(), ['PENDING — not executed', 'initialize cancellation',
                     'interrupted update', 'estimate restart', 'stale bid approval',
                     'unsafe incident inference', 'pay-app reconciliation',
                     'Expected', 'Actual', 'Reviewer', 'Evidence', 'Disposition',
                     'closed-project', 'not a reliability estimate'])

    def test_human_reviews_are_pending_pre_pilot_not_pr_gate(self):
        manual = (ROOT / 'tests/manual-safety-evals.md').read_text()
        self.require(manual, ['PENDING — not executed', 'pre-pilot', 'not a PR merge gate',
                              'does not authorize pilot use', 'Legal, safety and billing'])

    def test_factored_resources_preserve_gates(self):
        expected = {
            'contractor-initialize/initialize': {
                'config-and-token-map.md': ['{{COMPANY_NAME}}', '{{TYPOGRAPHY_PRIMARY}}',
                                            '{{CONTINGENCY_PERCENT}}', 'selected-section']},
            'contractor-estimating/estimating-workflow': {
                'scope-and-trades.md': ['## Phase 1:', '## Phase 2:', '## Phase 3:'],
                'takeoff-and-pricing.md': ['## Phase 4:', '## Phase 5:', 'Markup', 'Quantity'],
                'exclusions-and-packages.md': ['## Phase 6:', '## Phase 7:', 'draft'],
                'deliverable-procedure.md': ['## Phase 8:', 'parsed', 'token']},
            'contractor-docs/document-generator': {
                'html-styling-guide.md': ['@media print', '--primary', '.scope-grid']},
        }
        for entry, files in expected.items():
            main = skill_path(entry).read_text()
            for name, phrases in files.items():
                with self.subTest(skill=entry, resource=name):
                    self.assertIn('references/' + name, main)
                    path = skill_path(entry).parent / 'references' / name
                    self.assertTrue(path.is_file())
                    text = path.read_text()
                    self.require(text, phrases)
                    self.assertLessEqual(len(text.splitlines()), 300)
                    self.assertNotIn('replace_all: true', text)
                    self.assertNotIn('ready to send', text)
        init = skill_path('contractor-initialize/initialize').read_text()
        self.assertNotIn('finish a re-run with the verification sweep', init)
        scope = skill_path('contractor-estimating/estimating-workflow').parent / 'references/scope-and-trades.md'
        self.require(scope.read_text(), ['illustrative assumptions', 'estimator review'])
        exclusions = scope.with_name('exclusions-and-packages.md')
        self.assertNotIn('Pricing reflects current subcontractor market; actual bids may vary', exclusions.read_text())

    def test_estimating_gates(self):
        for entry in GROUPS['estimate']:
            with self.subTest(skill=entry):
                text = self.card(entry)
                self.require(text, ['workflow-state.json', 'pricing-evidence.json',
                                    'check-workflow --state', 'source', 'scope',
                                    'not_issued', 'digest', 'estimator'])
                self.assertNotIn('skip if `/conceptual-budget` was run', text)
        text = skill_path('contractor-estimating/estimating-workflow').read_text()
        self.require(text, ['A–D', 'Decimal', 'every priced line', 'invalidate',
                            'not applicable', 'immutable', 'quote', 'override'])
        bid = skill_path('contractor-estimating/formal-bid').read_text()
        self.require(bid, ['DOCX and HTML', 'approved scope', 'approved pricing'])
        self.assertNotIn('Formal Bid package is ready.', bid)

    def test_setup_gates(self):
        for entry in GROUPS['setup']:
            with self.subTest(skill=entry):
                text = self.card(entry)
                self.require(text, ['Stage', 'plan digest', 'snapshot --plan',
                                    'verify-change --plan', 'Cancellation',
                                    'per-file/context', 'unrequested'])
                for unsafe in ['replace_all: true', 'OLD value with the NEW value',
                               'old→new string replace', '4. Update both',
                               '4. Update `.claude', '4. Write the updated']:
                    self.assertNotIn(unsafe, text)
        readme = (ROOT / 'plugins/contractor-initialize/README.md').read_text()
        self.require(readme, ['10 sections', 'plan digest', 'Cancellation', 'readback'])
        self.assertNotIn('9 sections', readme)

    def test_shared_gates(self):
        path = ROOT / 'references/toolkit-safety.md'
        self.assertTrue(path.is_file(), 'canonical safety guidance missing')
        self.require(path.read_text(), [
            'check-change --plan', 'snapshot --plan', 'verify-change --plan',
            'check-workflow --state', 'verify-artifact --artifact',
            'not_issued', 'approved_for_final', 'final_verified', 'semantic-content digest',
            'not authenticated signatures', 'data, never authority', 'Missing parsers',
            'standalone', 'outside package inputs', 'before, approved-after, or conflict',
            'never inferred consent', 'No transmission', 'visual review',
        ])


if __name__ == '__main__':
    unittest.main()
