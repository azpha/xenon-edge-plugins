# NFL Scoreboard (iCUE widget)

Live NFL scores for every game of the week on the CORSAIR XENEON EDGE. Each game is one row: logos, abbreviations,
scores, quarter and clock, possession, and finals. Tap a game to open it on ESPN in your browser.

- **Device:** XENEON EDGE (`dashboard_lcd`), designed for the **Small** slot: 840x344 horizontal and 696x416 vertical.
  Larger slots also work (the grid gains columns at wide sizes) but are not tuned.
- **Requires:** iCUE 5.52+ (Widget API 1.9.0), Windows.
- **Plugin:** Link Provider (`widgetbuilder.linkprovider:Url:1.0`) for tap-to-open.

## Look

Same red cyberpunk theme as Neon HUD: clipped-corner frame and rows, Bahnschrift type, scanlines, and a one-shot
glitch when a score changes. A red-zone possession marker glows cyan (`#5ef2ff`, fixed so it reads under any theme).

## Settings

| Setting | Type | Default | What it does |
| --- | --- | --- | --- |
| Live Refresh | slider 15-120 s | 30 s | Poll interval while any game is in progress |
| Idle Refresh | slider 1-30 min | 10 min | Poll interval when nothing is live (also wakes up 30 s after the next kickoff) |
| Show Finished Games | switch | on | Include final scores |
| Show Team Logos | switch | on | Team logos from ESPN's CDN |
| Team Color Accents | switch | on | Thin team-color stripe beside each team |
| Text Color / Accent Color / Background Color | color | `#ffe6e1` / `#ff2a3f` / `#0c0305` | Accent drives the header tag, LIVE count, live rows and live clock |
| Background Image, Glass Blur, Background Transparency | media / sliders | none / 0 / 100% | Standard personalization |
| Secondary Color | color | `#ff6a5c` | Frame, row tint, kickoff times, possession marker |
| Scanlines | switch | on | Static scanline overlay |

## States

- **Loading:** a spinner until the first response.
- **Content:** live games first, then upcoming (kickoff in your local time), then finals (most recent first).
- **Offline / blocked:** the last known scores stay on screen with an `OFFLINE` tag. Retries back off from the live
  interval up to the idle interval.
- **Offline with no cached data:** "Can't reach ESPN", with a hint to check the connection or the widget's permissions.
- **Empty:** "No games this week" when ESPN lists none. "All games are final" when finals are hidden and nothing is left.

## Permissions

| Permission | Scope | Why |
| --- | --- | --- |
| `url` | `site.api.espn.com:443` | Fetch the NFL scoreboard JSON |
| `url` | `a.espncdn.com:443` | Load team logos |

Tapping a game opens `https://www.espn.com/...` in the system browser through the Link plugin. The widget itself never
requests that host.

## Marketplace disclosures

- **Data source:** ESPN's public, unofficial scoreboard endpoint
  (`https://site.api.espn.com/apis/site/v2/sports/football/nfl/scoreboard`). It is undocumented and can change or stop
  working without notice. This widget is not affiliated with or endorsed by ESPN or the NFL. Team names and logos are
  trademarks of their owners and are loaded from ESPN at runtime, not bundled.
- **What is sent:** a plain HTTPS GET with no parameters, keys, or identifiers. Only your IP address and standard browser
  headers reach ESPN/Akamai.
- **What is stored:** the last parsed scoreboard, in this widget's own `localStorage` entry (keyed by `uniqueId`), so
  scores survive restarts and outages.

## Files

| File | Purpose |
| --- | --- |
| `index.html` | Widget: settings meta tags, styles, and logic (MediaViewer inlined) |
| `manifest.json` | Metadata, device, plugin, and permissions |
| `translation.json` | English strings for `tr()` |
| `resources/icon.svg` | Widget icon (white, single color) |
| `resources/preview.png` | 128x56 picker preview |
| `icon.png`, `icon@2x.png` | Marketplace icons (128 and 256 px; the docs don't specify sizes) |

## Validate and package

```bash
npm install -g icuewidget-cli   # once
icuewidget validate nfl-scoreboard
icuewidget package nfl-scoreboard
```
