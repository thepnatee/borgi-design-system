# Motion Guidelines

Motion explains hierarchy, continuity and system status. It must not delay work.

## Durations
- Instant feedback: 80–120 ms
- Small transitions: 160–220 ms
- Page or large-surface transitions: 240–320 ms
- Celebrations: up to 600 ms, never blocking

## Curves
Use ease-out for entering, ease-in for leaving and standard ease-in-out for movement within the same context. Avoid exaggerated bounce in operational screens.

## Reduced motion
Respect `prefers-reduced-motion`. Replace movement with opacity changes and immediate state updates.

## Patterns
Buttons acknowledge press immediately. Modals fade with slight scale. Drawers translate from their edge. Skeletons avoid aggressive shimmer. Success animation plays once and keeps confirmation text visible.