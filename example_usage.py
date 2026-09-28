from client import ExecutiveBriefingSynthesizer

synthesizer = ExecutiveBriefingSynthesizer()
dossier = synthesizer.synthesize()
print("=== Executive Briefing Dossier ===")
print(f"Health Score: {dossier['health_score']}/100 | Department: {dossier['department']}")
print("Highlights:")
for h in dossier["highlights"]:
    print(f"  * {h}")
print("Risks:")
for r in dossier["risks"]:
    print(f"  ! [{r['impact']}] {r['risk']} (Owner: {r['owner']})")
