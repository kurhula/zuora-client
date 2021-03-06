# coding: utf-8




import pprint
import re  # noqa: F401

import six

from zuora_client.models.payment_debit_memo_application_item_create_request_type import PaymentDebitMemoApplicationItemCreateRequestType  # noqa: F401,E501


class PaymentDebitMemoApplicationCreateRequestType(object):
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
        'amount': 'float',
        'debit_memo_id': 'str',
        'items': 'list[PaymentDebitMemoApplicationItemCreateRequestType]'
    }

    attribute_map = {
        'amount': 'amount',
        'debit_memo_id': 'debitMemoId',
        'items': 'items'
    }

    def __init__(self, amount=None, debit_memo_id=None, items=None):  # noqa: E501
        """PaymentDebitMemoApplicationCreateRequestType - a model defined in Swagger"""  # noqa: E501

        self._amount = None
        self._debit_memo_id = None
        self._items = None
        self.discriminator = None

        self.amount = amount
        if debit_memo_id is not None:
            self.debit_memo_id = debit_memo_id
        if items is not None:
            self.items = items

    @property
    def amount(self):
        """Gets the amount of this PaymentDebitMemoApplicationCreateRequestType.  # noqa: E501

        The amount of the payment associated with the debit memo.   # noqa: E501

        :return: The amount of this PaymentDebitMemoApplicationCreateRequestType.  # noqa: E501
        :rtype: float
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this PaymentDebitMemoApplicationCreateRequestType.

        The amount of the payment associated with the debit memo.   # noqa: E501

        :param amount: The amount of this PaymentDebitMemoApplicationCreateRequestType.  # noqa: E501
        :type: float
        """
        if amount is None:
            raise ValueError("Invalid value for `amount`, must not be `None`")  # noqa: E501

        self._amount = amount

    @property
    def debit_memo_id(self):
        """Gets the debit_memo_id of this PaymentDebitMemoApplicationCreateRequestType.  # noqa: E501

        The unique ID of the debit memo that the payment is created on.   # noqa: E501

        :return: The debit_memo_id of this PaymentDebitMemoApplicationCreateRequestType.  # noqa: E501
        :rtype: str
        """
        return self._debit_memo_id

    @debit_memo_id.setter
    def debit_memo_id(self, debit_memo_id):
        """Sets the debit_memo_id of this PaymentDebitMemoApplicationCreateRequestType.

        The unique ID of the debit memo that the payment is created on.   # noqa: E501

        :param debit_memo_id: The debit_memo_id of this PaymentDebitMemoApplicationCreateRequestType.  # noqa: E501
        :type: str
        """

        self._debit_memo_id = debit_memo_id

    @property
    def items(self):
        """Gets the items of this PaymentDebitMemoApplicationCreateRequestType.  # noqa: E501

        Container for debit memo items.  **Note:** The Invoice Item Settlement feature is in **Limited Availability**. If you wish to have access to the feature, submit a request at [Zuora Global Support](http://support.zuora.com/).   # noqa: E501

        :return: The items of this PaymentDebitMemoApplicationCreateRequestType.  # noqa: E501
        :rtype: list[PaymentDebitMemoApplicationItemCreateRequestType]
        """
        return self._items

    @items.setter
    def items(self, items):
        """Sets the items of this PaymentDebitMemoApplicationCreateRequestType.

        Container for debit memo items.  **Note:** The Invoice Item Settlement feature is in **Limited Availability**. If you wish to have access to the feature, submit a request at [Zuora Global Support](http://support.zuora.com/).   # noqa: E501

        :param items: The items of this PaymentDebitMemoApplicationCreateRequestType.  # noqa: E501
        :type: list[PaymentDebitMemoApplicationItemCreateRequestType]
        """

        self._items = items

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
        if issubclass(PaymentDebitMemoApplicationCreateRequestType, dict):
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
        if not isinstance(other, PaymentDebitMemoApplicationCreateRequestType):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
