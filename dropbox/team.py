# Auto-generated by BabelAPI, do not modify.
try:
    from . import babel_validators as bv
except (SystemError, ValueError):
    # Catch errors raised when importing a relative module when not in a package.
    # This makes testing this file directly (outside of a package) easier.
    import babel_validators as bv

class GroupSummary(object):
    """
    Information about a group.

    :ivar group_external_id: External ID of group. This is an arbitrary ID that
        an admin can attach to a group.
    :ivar member_count: The number of members in the group.
    """

    __slots__ = [
        '_group_name_value',
        '_group_name_present',
        '_group_id_value',
        '_group_id_present',
        '_group_external_id_value',
        '_group_external_id_present',
        '_member_count_value',
        '_member_count_present',
    ]

    _has_required_fields = True

    def __init__(self,
                 group_name=None,
                 group_id=None,
                 member_count=None,
                 group_external_id=None):
        self._group_name_value = None
        self._group_name_present = False
        self._group_id_value = None
        self._group_id_present = False
        self._group_external_id_value = None
        self._group_external_id_present = False
        self._member_count_value = None
        self._member_count_present = False
        if group_name is not None:
            self.group_name = group_name
        if group_id is not None:
            self.group_id = group_id
        if group_external_id is not None:
            self.group_external_id = group_external_id
        if member_count is not None:
            self.member_count = member_count

    @property
    def group_name(self):
        """
        :rtype: str
        """
        if self._group_name_present:
            return self._group_name_value
        else:
            raise AttributeError("missing required field 'group_name'")

    @group_name.setter
    def group_name(self, val):
        val = self._group_name_validator.validate(val)
        self._group_name_value = val
        self._group_name_present = True

    @group_name.deleter
    def group_name(self):
        self._group_name_value = None
        self._group_name_present = False

    @property
    def group_id(self):
        """
        :rtype: str
        """
        if self._group_id_present:
            return self._group_id_value
        else:
            raise AttributeError("missing required field 'group_id'")

    @group_id.setter
    def group_id(self, val):
        val = self._group_id_validator.validate(val)
        self._group_id_value = val
        self._group_id_present = True

    @group_id.deleter
    def group_id(self):
        self._group_id_value = None
        self._group_id_present = False

    @property
    def group_external_id(self):
        """
        External ID of group. This is an arbitrary ID that an admin can attach
        to a group.

        :rtype: str
        """
        if self._group_external_id_present:
            return self._group_external_id_value
        else:
            return None

    @group_external_id.setter
    def group_external_id(self, val):
        if val is None:
            del self.group_external_id
            return
        val = self._group_external_id_validator.validate(val)
        self._group_external_id_value = val
        self._group_external_id_present = True

    @group_external_id.deleter
    def group_external_id(self):
        self._group_external_id_value = None
        self._group_external_id_present = False

    @property
    def member_count(self):
        """
        The number of members in the group.

        :rtype: long
        """
        if self._member_count_present:
            return self._member_count_value
        else:
            raise AttributeError("missing required field 'member_count'")

    @member_count.setter
    def member_count(self, val):
        val = self._member_count_validator.validate(val)
        self._member_count_value = val
        self._member_count_present = True

    @member_count.deleter
    def member_count(self):
        self._member_count_value = None
        self._member_count_present = False

    def __repr__(self):
        return 'GroupSummary(group_name={!r}, group_id={!r}, member_count={!r}, group_external_id={!r})'.format(
            self._group_name_value,
            self._group_id_value,
            self._member_count_value,
            self._group_external_id_value,
        )

GroupSummary._group_name_validator = bv.String()
GroupSummary._group_id_validator = bv.String()
GroupSummary._group_external_id_validator = bv.Nullable(bv.String())
GroupSummary._member_count_validator = bv.UInt32()
GroupSummary._all_field_names_ = set([
    'group_name',
    'group_id',
    'group_external_id',
    'member_count',
])
GroupSummary._all_fields_ = [
    ('group_name', GroupSummary._group_name_validator),
    ('group_id', GroupSummary._group_id_validator),
    ('group_external_id', GroupSummary._group_external_id_validator),
    ('member_count', GroupSummary._member_count_validator),
]
