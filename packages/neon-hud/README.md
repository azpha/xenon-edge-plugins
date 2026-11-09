# Neon HUD (iCUE widget)

A full-screen neon cyberpunk dashboard for the CORSAIR XENEON EDGE: live sensor gauges, FPS with a 60-second history,
now-playing music with touch controls, a clock, and a notification counter.

- **Device:** XENEON EDGE (`dashboard_lcd`), designed for **Extra Large horizontal (2536x696)**, the whole screen.
  Narrower slots hide panels instead of shrinking them: below 2100px the FPS panel goes, below 1500px the clock,
  and below 1000px the music player. Vertical slots are not designed for.
- **Requires:** iCUE 5.52+ (Widget API 1.9.0: Media 1.1 and Notifications), Windows.
- **Touch:** `interactive: true`, for the previous / play-pause / next buttons.

## Panels

| Panel | Source | Notes |
| --- | --- | --- |
| CHRONO | Local clock + Notifications plugin | 12/24 h, optional seconds; the counter glitches once when new notifications arrive |
| SYS.MONITOR | Sensors plugin | 4 gauges. Bars are the secondary color, turn amber (`#ffb347`) near the limit and cyan (`#5ef2ff`) at it. These status colors are fixed so they stay readable under any theme: temps from the warning setting (converted when iCUE uses F), loads at 95%. RPM and other units scale to the peak seen |
| FRAME.RATE | FPS plugin | Current FPS, 60 s sparkline (gaps where FPS is unavailable), and the foreground process |
| AUDIO.LINK | Media plugin 1.1 | Album art, title, artist and album, playing/paused state, and previous / play-pause / next |

## Settings

| Setting | Type | Default |
| --- | --- | --- |
| Sensor 1-4 | sensors-combobox | CPU temp, GPU temp, CPU load (`load`/`package`), GPU load (iCUE picks the closest match) |
| Temperature Warning | slider 50-110 C | 85 C |
| 24-Hour Clock / Show Seconds | switch | off / off |
| Text / Accent / Background Color | color | `#ffe6e1` / `#ff2a3f` / `#0c0305` |
| Background Image, Glass Blur, Background Transparency | media / slider / slider | none / 0 / 100% |
| Secondary Color | color | `#ff6a5c` |
| Scanlines | switch | on |

Motion is subtle: static scanlines, a one-shot glitch on track change, warning crossings, new notifications and
process changes, and eased gauge segments. Reduced-motion is respected.

## States

- **No sensor picked:** "NO SENSOR / Pick a sensor in widget settings".
- **Sensor disconnected or removed:** "Sensor offline". It re-binds automatically when the sensor comes back.
- **No media session:** "NO SIGNAL / Start playback in any media app". The controls stay active.
- **No FPS for the current app:** dimmed `--` with "No FPS data for this app". The process name stays visible.
- **Plugin not ready:** each panel shows NO SIGNAL until its plugin initializes (checked for 30 s after load).
- **Opened in a plain browser:** labeled `DEMO DATA` with simulated values. This never runs inside iCUE.

## Permissions

None required. The widget makes no network requests and reads no files. The Sensors, Media, FPS and Notifications
plugins document no permission requirement.

## Marketplace notes

- **Original design:** neon colors, clipped panels and glitch effects in the generic cyberpunk style. No third-party
  logos, fonts or names. Text uses Windows' built-in Bahnschrift font, nothing is bundled or downloaded.
- **Data:** everything stays on the PC. Sensor values, track info and notification counts come from iCUE plugins and
  are only rendered. Nothing is stored or sent anywhere.

## Implementation notes

- **Plugin calls:** made directly through the documented `requestId` + `asyncResponse` pattern. The
  `common/plugins/*Wrapper.js` files aren't in the docs bundle, and iCUE blocks external scripts for user widgets.
- **Notifications:** the docs list `getNotificationCount()` without a `requestId`, so the widget accepts either a direct
  return value or an `asyncResponse` reply. Confirm on device.
