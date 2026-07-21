# Figma Mapping

## Pages

`00 Cover`, `01 Foundations`, `02 Components`, `03 Patterns`, `04 Customer`, `05 Admin`, `06 Marketing`, `07 Mascot`, `08 Illustrations`, `09 Archive`.

## Naming

Components use `Category/Component/Variant/State`, for example `Form/Input/Text/Error`. Frames use `Platform/Module/Screen/State`. Variables mirror `tokens/tokens.json` names and modes.

## Requirements

- Components use Auto Layout and published properties.
- Colors, spacing, radius, typography and elevation use variables rather than detached values.
- Interactive states include default, hover, focus, pressed, disabled, loading and error where relevant.
- Screen frames link to their matching repository specification.
- Exported assets use lowercase kebab-case and include scale or purpose only when required.
- Deprecated components move to Archive and are not silently deleted.
