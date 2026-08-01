# AEC CP
## AEC Automation + AI Engineering Portfolio

**Goal:** ASE | 20-week build
**Stack:** Python, HTML/CSS/JS, FastAPI, Anthropic AI, Autodesk APS
**Started:** May 2026

---

## Dev Log

### Day 7 | August 1, 2026

- Completed AEC CP beta 3.0 | full build session, single-file HTML5 VIF coordination platform
- Built 4-shape AEC orb | Canvas 2D dot-sphere morphs into I-beam, curtain wall unit, terracotta panel, and drainage pipes on hover
- Implemented frosted glass UI system | all interactive surfaces use backdrop-filter blur, zero solid boxes
- Built custom dropdown system replacing all native select elements | glass pill trigger, frosted options panel, iOS touch-compatible
- Replaced all 11 native alert() calls with in-DOM toast system | works in sandboxed iframe and iOS PWA contexts
- Implemented animated input underline | focus grows 1.5px line left to right via background-size CSS transition
- Built 3-dot menu animation | 3 span elements animate into X shape on open with spring cubic-bezier
- Added letter-by-letter subtitle animation scoped to home screen only
- Removed light mode | dark-only theme, #0a0a09 background
- Stack: HTML/CSS/JS | vanilla, no frameworks, offline-capable and cellular-ready
- Status: Beta 3.0 | closed source, active development

### Day 6 | July 25, 2026

- Built complete VIF request CRUD | sender, receiver, trade, job number, date, description, status tracking
- Built project management system | create, switch, archive projects with PRO PLAN enforcement
- Built team roster module | member name, role, trade, photo upload via FileReader API stored as base64
- Implemented localStorage persistence with safeGet/safeSet wrappers | crash-safe in sandboxed contexts
- Built screen state machine | showScreen() with surfaceRise keyframe animation (scale, translateY, blur resolve)
- Fixed critical orb tap-blocking bug | invisible scaled canvas intercepting all touch events post-animation
- Fixed localStorage crash in sandboxed iframes | wrapped all access in try/catch safety wrappers
- Fixed dot canvas rendering black after light mode removal | hardcoded base=255 in both canvas renderers
- Stack: HTML/CSS/JS | single file, runs offline on iPhone and desktop
- Status: Beta | closed source, active development

### Day 5 | July 25, 2026

- Designed AEC CP visual system | frosted glass language, CSS custom property system, dark-only palette
- Built animated background dot field | full-screen Canvas 2D with wave motion, white micro-dots
- Built home orb | rotating 3D dot-sphere on Canvas 2D with hover morphing architecture
- Established orb nav reveal interaction | tap orb triggers scale(13) zoom, nav buttons surface after animation
- Built ghost date field and ghost job number field | faded placeholder style, consistent across form fields
- Established git commit convention | feat/fix/style prefix pattern for all future commits
- Stack: HTML/CSS/JS, Canvas 2D API
- Status: Beta | closed source, active development

### Day 4 | May 23, 2026 – July 2026

- Continued AEC CP development across extended session
- Refined VIF coordination workflow | open, in-progress, closed status pipeline
- Built change order tracking module
- Multi-format export pipeline | xlsx, csv, json, txt
- AI cost analysis module integrated | live Claude API replacing mock response
- localStorage persistence | projects survive browser close
- Stack: HTML/CSS/JS, Anthropic Claude API, offline-first architecture
- Status: Beta | closed source, active development

### Day 3 | May 23, 2026

- Expanded natural language input | full keyword coverage across all materials and subtypes
- Added natural language input to Builder tab | 29 room types, dimension and material parsing
- Wired live Claude API integration | real AI cost analysis replacing mock response
- API key stored in localStorage | secure, persistent, never hardcoded
- Ran local HTTP server for API compatibility | python http.server workflow established
- Stack: HTML/CSS/JS, Anthropic Claude API, offline-first architecture
- Status: Beta | closed source, active development

### Day 2 | May 23, 2026

- Continued AEC CP development | browser-based AEC field tool
- Integrated AI-powered estimate analysis module
- Built custom UI components | date picker, modal system
- Multi-format export pipeline | xlsx, csv, json, txt
- localStorage persistence | projects survive browser close
- Stack: HTML/CSS/JS, Anthropic AI, offline-first architecture
- Status: Beta | closed source, active development

### Day 1 | May 17, 2026

- Built AEC unit converter CLI with 6 conversion types and menu
- Built AEC project cost estimator with material pricing and report output
- Built AEC CSV reader | auto cost report from room data file
- Built report export | full data pipeline: CSV in, report.txt out
- Built FastAPI endpoint | AEC cost estimator live on web at /estimate
- Built AEC CP Room Builder | interactive input, auto CSV + report export
- Set up GitHub, VS Code, Git authentication | full dev environment live

---

## Projects

- `aec_converter.py` | AEC unit converter (ft/m, sqft/sqm, in/mm)
- `aec_cost_estimator.py` | Room cost estimator (drywall, tile, concrete)
- `aec_csv_reader.py` | CSV data pipeline, auto project cost report
- `aec_api.py` | FastAPI web endpoint, AEC cost estimator API
- `aec_room_builder.py` | Interactive room builder, auto CSV + report
- `report.txt` | Auto-generated AEC project cost report
- `rooms.csv` | Sample room data (Revit export format)

Note: select projects and modules may be integrated into a future desktop version of AEC CP.

---

## AEC CP Tool (Closed Source)

Browser-based AEC field coordination platform | offline-capable and cellular-ready for active field use, zero dependencies, zero install. Core workflow: create and track VIF (Verify In Field) requests with sender, receiver, trade, job number, status, and description. Features: project management with archive, team roster with photo upload, PRO PLAN enforcement, AI cost analysis, multi-format export (xlsx, csv, json, txt), custom dropdown and modal system, frosted glass UI, animated 3D AEC orb (I-beam, curtain wall, terracotta panel, drainage pipes), localStorage persistence. Status: Beta 3.0 | closed source, not public. Stack: HTML/CSS/JS | single self-contained file, runs in any browser on iPhone or desktop. Roadmap: native desktop app version and expanded platform sections under consideration.