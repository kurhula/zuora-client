# coding: utf-8




import pprint
import re  # noqa: F401

import six

from zuora_client.models.journal_entry_item_object_custom_fields import JournalEntryItemObjectCustomFields  # noqa: F401,E501


class GETJournalEntryItemType(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'accounting_code_name': 'str',
        'accounting_code_type': 'str',
        'amount': 'str',
        'gl_account_name': 'str',
        'gl_account_number': 'str',
        'home_currency_amount': 'str',
        'type': 'str'
    }

    attribute_map = {
        'accounting_code_name': 'accountingCodeName',
        'accounting_code_type': 'accountingCodeType',
        'amount': 'amount',
        'gl_account_name': 'glAccountName',
        'gl_account_number': 'glAccountNumber',
        'home_currency_amount': 'homeCurrencyAmount',
        'type': 'type'
    }

    def __init__(self, accounting_code_name=None, accounting_code_type=None, amount=None, gl_account_name=None, gl_account_number=None, home_currency_amount=None, type=None):  # noqa: E501
        """GETJournalEntryItemType - a model defined in Swagger"""  # noqa: E501

        self._accounting_code_name = None
        self._accounting_code_type = None
        self._amount = None
        self._gl_account_name = None
        self._gl_account_number = None
        self._home_currency_amount = None
        self._type = None
        self.discriminator = None

        if accounting_code_name is not None:
            self.accounting_code_name = accounting_code_name
        if accounting_code_type is not None:
            self.accounting_code_type = accounting_code_type
        if amount is not None:
            self.amount = amount
        if gl_account_name is not None:
            self.gl_account_name = gl_account_name
        if gl_account_number is not None:
            self.gl_account_number = gl_account_number
        if home_currency_amount is not None:
            self.home_currency_amount = home_currency_amount
        if type is not None:
            self.type = type

    @property
    def accounting_code_name(self):
        """Gets the accounting_code_name of this GETJournalEntryItemType.  # noqa: E501

        Name of the accounting code.   # noqa: E501

        :return: The accounting_code_name of this GETJournalEntryItemType.  # noqa: E501
        :rtype: str
        """
        return self._accounting_code_name

    @accounting_code_name.setter
    def accounting_code_name(self, accounting_code_name):
        """Sets the accounting_code_name of this GETJournalEntryItemType.

        Name of the accounting code.   # noqa: E501

        :param accounting_code_name: The accounting_code_name of this GETJournalEntryItemType.  # noqa: E501
        :type: str
        """

        self._accounting_code_name = accounting_code_name

    @property
    def accounting_code_type(self):
        """Gets the accounting_code_type of this GETJournalEntryItemType.  # noqa: E501

        Accounting code type.  Note that `On-Account Receivable` is only available if you enable the Invoice Settlement feature.    # noqa: E501

        :return: The accounting_code_type of this GETJournalEntryItemType.  # noqa: E501
        :rtype: str
        """
        return self._accounting_code_type

    @accounting_code_type.setter
    def accounting_code_type(self, accounting_code_type):
        """Sets the accounting_code_type of this GETJournalEntryItemType.

        Accounting code type.  Note that `On-Account Receivable` is only available if you enable the Invoice Settlement feature.    # noqa: E501

        :param accounting_code_type: The accounting_code_type of this GETJournalEntryItemType.  # noqa: E501
        :type: str
        """
        allowed_values = ["AccountsReceivable", "On-Account Receivable", "Cash", "OtherAssets", "CustomerCashOnAccount", "DeferredRevenue", "SalesTaxPayable", "OtherLiabilities", "SalesRevenue", "SalesDiscounts", "OtherRevenue", "OtherEquity", "BadDebt", "OtherExpenses"]  # noqa: E501
        if accounting_code_type not in allowed_values:
            raise ValueError(
                "Invalid value for `accounting_code_type` ({0}), must be one of {1}"  # noqa: E501
                .format(accounting_code_type, allowed_values)
            )

        self._accounting_code_type = accounting_code_type

    @property
    def amount(self):
        """Gets the amount of this GETJournalEntryItemType.  # noqa: E501

        Journal entry item amount in transaction currency.   # noqa: E501

        :return: The amount of this GETJournalEntryItemType.  # noqa: E501
        :rtype: str
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this GETJournalEntryItemType.

        Journal entry item amount in transaction currency.   # noqa: E501

        :param amount: The amount of this GETJournalEntryItemType.  # noqa: E501
        :type: str
        """

        self._amount = amount

    @property
    def gl_account_name(self):
        """Gets the gl_account_name of this GETJournalEntryItemType.  # noqa: E501

        The account number in the general ledger (GL) that corresponds to the accounting code.   # noqa: E501

        :return: The gl_account_name of this GETJournalEntryItemType.  # noqa: E501
        :rtype: str
        """
        return self._gl_account_name

    @gl_account_name.setter
    def gl_account_name(self, gl_account_name):
        """Sets the gl_account_name of this GETJournalEntryItemType.

        The account number in the general ledger (GL) that corresponds to the accounting code.   # noqa: E501

        :param gl_account_name: The gl_account_name of this GETJournalEntryItemType.  # noqa: E501
        :type: str
        """

        self._gl_account_name = gl_account_name

    @property
    def gl_account_number(self):
        """Gets the gl_account_number of this GETJournalEntryItemType.  # noqa: E501

        The account name in the general ledger (GL) that corresponds to the accounting code.   # noqa: E501

        :return: The gl_account_number of this GETJournalEntryItemType.  # noqa: E501
        :rtype: str
        """
        return self._gl_account_number

    @gl_account_number.setter
    def gl_account_number(self, gl_account_number):
        """Sets the gl_account_number of this GETJournalEntryItemType.

        The account name in the general ledger (GL) that corresponds to the accounting code.   # noqa: E501

        :param gl_account_number: The gl_account_number of this GETJournalEntryItemType.  # noqa: E501
        :type: str
        """

        self._gl_account_number = gl_account_number

    @property
    def home_currency_amount(self):
        """Gets the home_currency_amount of this GETJournalEntryItemType.  # noqa: E501

        Journal entry item amount in home currency.   # noqa: E501

        :return: The home_currency_amount of this GETJournalEntryItemType.  # noqa: E501
        :rtype: str
        """
        return self._home_currency_amount

    @home_currency_amount.setter
    def home_currency_amount(self, home_currency_amount):
        """Sets the home_currency_amount of this GETJournalEntryItemType.

        Journal entry item amount in home currency.   # noqa: E501

        :param home_currency_amount: The home_currency_amount of this GETJournalEntryItemType.  # noqa: E501
        :type: str
        """

        self._home_currency_amount = home_currency_amount

    @property
    def type(self):
        """Gets the type of this GETJournalEntryItemType.  # noqa: E501

        Type of journal entry item.   # noqa: E501

        :return: The type of this GETJournalEntryItemType.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this GETJournalEntryItemType.

        Type of journal entry item.   # noqa: E501

        :param type: The type of this GETJournalEntryItemType.  # noqa: E501
        :type: str
        """
        allowed_values = ["Credit", "Debit"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(GETJournalEntryItemType, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, GETJournalEntryItemType):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
