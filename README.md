# SkyDock

SkyDock is an autonomous VTOL aircraft powered by ArduPilot for low-altitude, long-range missions. Features include simulated autonomous recharging and chemical refilling, a scanning/spraying FSM, and integrations with Hailo detection pipelines.

---

## Repository layout (important folders)

- /home/fred/skydock/software/
  - fsm/
    - template.py — Finite State Machine for drone mission logic (states described below).
  - telemetry.py — telemetry singleton (expected: `telm_singleton.run_pre_flight_checks()`).
  - move.py — movement singleton (expected: `move_singleton.arm_and_take_off_to_hight(h)`, `move_singleton.fly_to_point(lat, lon, alt_above_home)`, `move_singleton.set_mode(m)`, `move_singleton.get_mode()`).
  - ai.py — AI/frame storage (expected: `ai_storage_singleton.get_frames_in_time_period(...)`, and `Camera`).
  - drone_snapshots.py — snapshot helpers and planner (expected: `drone_telm_stapshot` with `altitude_rel_home`, `latitude`, `longitude`; `ScanningPlanner.next_point(loc)` and `ScanningPlanner.scan_alt`; `Weed`, `WeedStorage` helpers).
  - tests/ — pytest-compatible test suite for the FSM and module integration.

---

## Code documentation (software/)

- fsm/template.py
  - FSM: lightweight manager with current `state`.
  - DroneState (Protocol): `enter()`, `update()`, `exit()`.
  - Context: mission-wide flags like `take_off_hight` and `scaning_complete`.
  - OnGroundState:
    - enter: logs presence on ground.
    - update: checks pre-flight via `telm_singleton` and asks ground control via `GroundStaionMessages.ask_gc_question(...)`; on permission, calls `move_singleton.arm_and_take_off_to_hight(Context.take_off_hight)` and returns `TakeOff`.
  - TakeOff:
    - enter: asks permission and may call `arm_and_take_off_to_hight`.
    - update: checks `drone_telm_stapshot.altitude_rel_home` against `Context.take_off_hight` and routes to `Scaning` or spraying FSM.
  - Scaning:
    - update: queries `ScanningPlanner.next_point(loc)`. If None, sets `Context.scaning_complete = True` and returns `Spraying`. Otherwise flies to the next point and collects frames from `ai_storage_singleton` and obtains weeds via `Weed.retun_all_new_valid_weeds(...)`, then stores them in `WeedStorage`.
  - RetunToHome:
    - enter: sets mode to "RTH"; update ensures mode remains "RTH".
  - Spraying: placeholder — implement spray sub-states (fly-to-point, spray, return) as needed.

- telemetry.py / move.py / ai.py / drone_snapshots.py
  - The FSM expects simple singletons and lightweight APIs (see above). Tests mock these singletons to avoid hardware interactions.

---

## Hailo integration notes (manual edits)

- Replace file:
  - Path: `software/hailo-apps-infra/hailo_apps/hailo_app_python/apps/detection/detection.py`
  - Replace its contents with the provided detection app code that forwards detections into the local `ai` storage (see original README snippet).
- Edit core CLI default:
  - File: `software/hailo-apps-infra/hailo_apps/hailo_app_python/core/common/core.py`
  - Change the CLI default to:
    - `"--input", "-i", type=str, default="rpi",`
- setproctitle:
  - If present, comment out uses of `setproctitle` to avoid issues on some systems.

---

## Notes and best practices

- Keep hardware singletons isolated behind small wrapper modules so unit tests can monkeypatch them (tests already mock `move_singleton`, `telm_singleton`, etc.).
- Implement and document the Spraying FSM before running live missions.
- Update this README when interfaces for singletons change.