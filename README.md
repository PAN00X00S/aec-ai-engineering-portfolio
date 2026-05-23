# ARCFORGE
### AEC Automation + AI Engineering Portfolio

**Goal:** ASE | 20-week build
**Stack:** Python, HTML/CSS/JS, FastAPI, Anthropic AI, Autodesk APS
**Started:** May 2026

---

## Dev Log

### Day 2 — May 23, 2026
- Continued ARCFORGE development — browser-based AEC field tool
- Integrated AI-powered estimate analysis module
- Built custom UI components — date picker, modal system
- Multi-format export pipeline — xlsx, csv, json, txt
- localStorage persistence — projects survive browser close
- Stack: HTML/CSS/JS, Anthropic AI, offline-first architecture
- Status: Beta — closed source, active development

### Day 1 — May 17, 2026
- Built AEC unit converter CLI with 6 conversion types and menu
- Built AEC project cost estimator with material pricing and report output
- Built AEC CSV reader — auto cost report from room data file
- Built report export — full data pipeline: CSV in, report.txt out
- Built FastAPI endpoint — AEC cost estimator live on web at /estimate
- Built ARCFORGE Room Builder — interactive input, auto CSV + report export
- Set up GitHub, VS Code, Git authentication — full dev environment live

---

## Projects
- `aec_converter.py` — AEC unit converter (ft/m, sqft/sqm, in/mm)
- `aec_cost_estimator.py` — Room cost estimator (drywall, tile, concrete)
- `aec_csv_reader.py` — CSV data pipeline, auto project cost report
- `aec_api.py` — FastAPI web endpoint, AEC cost estimator API
- `aec_room_builder.py` — Interactive room builder, auto CSV + report
- `report.txt` — Auto-generated AEC project cost report
- `rooms.csv` — Sample room data (Revit export format)

---

## ARCFORGE Tool (Closed Source)
Browser-based AEC field coordination tool — offline, zero dependencies.
Features: unit conversion, material estimation, change order tracking, multi-format export.
Status: In active development — closed source, not public.
Stack: HTML/CSS/JS — single file, runs in any browser.