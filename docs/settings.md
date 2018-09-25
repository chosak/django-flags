# Settings

## Defining flags

### `FLAGS`

Default: `{}`

A dictionary of available feature flags and optional conditions. Flags *must* be defined in this dictionary to be available to check and to add/remove conditions in the Django Admin.

This dictionary takes the following format:

```python
FLAGS = {
  'FLAG_WITH_EMPTY_CONDITIONS': {}
  'FLAG_WITH_CONDITIONS': {
    'condition name': 'value flag is expected to match to be enabled',
  }
}
```

### `FLAGS_SOURCES`

Default: `('flags.sources.SettingsFlagsSource', 'flags.sources.DatabaseFlagsSource',)`

A list or tuple containing the full Python path strings to classes that provides a [`get_flags()` method](api/sources/#flag-sources). The `get_flags()` method is expected to return a dictionary of flags and [`Condition` objects](api/sources/#conditioncondition-value-sourcenone-objnone). All flags returned by all flag sources will be available to check.