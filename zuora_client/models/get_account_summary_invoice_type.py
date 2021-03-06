# coding: utf-8




import pprint
import re  # noqa: F401

import six


class GETAccountSummaryInvoiceType(object):
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
        'amount': 'str',
        'balance': 'str',
        'due_date': 'date',
        'id': 'str',
        'invoice_date': 'date',
        'invoice_number': 'str',
        'status': 'str'
    }

    attribute_map = {
        'amount': 'amount',
        'balance': 'balance',
        'due_date': 'dueDate',
        'id': 'id',
        'invoice_date': 'invoiceDate',
        'invoice_number': 'invoiceNumber',
        'status': 'status'
    }

    def __init__(self, amount=None, balance=None, due_date=None, id=None, invoice_date=None, invoice_number=None, status=None):  # noqa: E501
        """GETAccountSummaryInvoiceType - a model defined in Swagger"""  # noqa: E501

        self._amount = None
        self._balance = None
        self._due_date = None
        self._id = None
        self._invoice_date = None
        self._invoice_number = None
        self._status = None
        self.discriminator = None

        if amount is not None:
            self.amount = amount
        if balance is not None:
            self.balance = balance
        if due_date is not None:
            self.due_date = due_date
        if id is not None:
            self.id = id
        if invoice_date is not None:
            self.invoice_date = invoice_date
        if invoice_number is not None:
            self.invoice_number = invoice_number
        if status is not None:
            self.status = status

    @property
    def amount(self):
        """Gets the amount of this GETAccountSummaryInvoiceType.  # noqa: E501

        Invoice amount before adjustments, discounts, and similar items.   # noqa: E501

        :return: The amount of this GETAccountSummaryInvoiceType.  # noqa: E501
        :rtype: str
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this GETAccountSummaryInvoiceType.

        Invoice amount before adjustments, discounts, and similar items.   # noqa: E501

        :param amount: The amount of this GETAccountSummaryInvoiceType.  # noqa: E501
        :type: str
        """

        self._amount = amount

    @property
    def balance(self):
        """Gets the balance of this GETAccountSummaryInvoiceType.  # noqa: E501

        Balance due on the invoice.   # noqa: E501

        :return: The balance of this GETAccountSummaryInvoiceType.  # noqa: E501
        :rtype: str
        """
        return self._balance

    @balance.setter
    def balance(self, balance):
        """Sets the balance of this GETAccountSummaryInvoiceType.

        Balance due on the invoice.   # noqa: E501

        :param balance: The balance of this GETAccountSummaryInvoiceType.  # noqa: E501
        :type: str
        """

        self._balance = balance

    @property
    def due_date(self):
        """Gets the due_date of this GETAccountSummaryInvoiceType.  # noqa: E501

        Due date as `yyyy-mm-dd`.   # noqa: E501

        :return: The due_date of this GETAccountSummaryInvoiceType.  # noqa: E501
        :rtype: date
        """
        return self._due_date

    @due_date.setter
    def due_date(self, due_date):
        """Sets the due_date of this GETAccountSummaryInvoiceType.

        Due date as `yyyy-mm-dd`.   # noqa: E501

        :param due_date: The due_date of this GETAccountSummaryInvoiceType.  # noqa: E501
        :type: date
        """

        self._due_date = due_date

    @property
    def id(self):
        """Gets the id of this GETAccountSummaryInvoiceType.  # noqa: E501

        Invoice ID.   # noqa: E501

        :return: The id of this GETAccountSummaryInvoiceType.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this GETAccountSummaryInvoiceType.

        Invoice ID.   # noqa: E501

        :param id: The id of this GETAccountSummaryInvoiceType.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def invoice_date(self):
        """Gets the invoice_date of this GETAccountSummaryInvoiceType.  # noqa: E501

        Invoice date as `yyyy-mm-dd`.   # noqa: E501

        :return: The invoice_date of this GETAccountSummaryInvoiceType.  # noqa: E501
        :rtype: date
        """
        return self._invoice_date

    @invoice_date.setter
    def invoice_date(self, invoice_date):
        """Sets the invoice_date of this GETAccountSummaryInvoiceType.

        Invoice date as `yyyy-mm-dd`.   # noqa: E501

        :param invoice_date: The invoice_date of this GETAccountSummaryInvoiceType.  # noqa: E501
        :type: date
        """

        self._invoice_date = invoice_date

    @property
    def invoice_number(self):
        """Gets the invoice_number of this GETAccountSummaryInvoiceType.  # noqa: E501

        Invoice number.   # noqa: E501

        :return: The invoice_number of this GETAccountSummaryInvoiceType.  # noqa: E501
        :rtype: str
        """
        return self._invoice_number

    @invoice_number.setter
    def invoice_number(self, invoice_number):
        """Sets the invoice_number of this GETAccountSummaryInvoiceType.

        Invoice number.   # noqa: E501

        :param invoice_number: The invoice_number of this GETAccountSummaryInvoiceType.  # noqa: E501
        :type: str
        """

        self._invoice_number = invoice_number

    @property
    def status(self):
        """Gets the status of this GETAccountSummaryInvoiceType.  # noqa: E501

        Invoice status - not the payment status of the invoice, just the status of the invoice itself. Possible values are: `Posted`, `Draft`, `Canceled`, `Error`.   # noqa: E501

        :return: The status of this GETAccountSummaryInvoiceType.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this GETAccountSummaryInvoiceType.

        Invoice status - not the payment status of the invoice, just the status of the invoice itself. Possible values are: `Posted`, `Draft`, `Canceled`, `Error`.   # noqa: E501

        :param status: The status of this GETAccountSummaryInvoiceType.  # noqa: E501
        :type: str
        """

        self._status = status

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
        if issubclass(GETAccountSummaryInvoiceType, dict):
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
        if not isinstance(other, GETAccountSummaryInvoiceType):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
