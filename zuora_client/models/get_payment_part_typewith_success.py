# coding: utf-8




import pprint
import re  # noqa: F401

import six


class GETPaymentPartTypewithSuccess(object):
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
        'created_by_id': 'str',
        'created_date': 'datetime',
        'debit_memo_id': 'str',
        'id': 'str',
        'invoice_id': 'str',
        'updated_by_id': 'str',
        'updated_date': 'datetime'
    }

    attribute_map = {
        'amount': 'amount',
        'created_by_id': 'createdById',
        'created_date': 'createdDate',
        'debit_memo_id': 'debitMemoId',
        'id': 'id',
        'invoice_id': 'invoiceId',
        'updated_by_id': 'updatedById',
        'updated_date': 'updatedDate'
    }

    def __init__(self, amount=None, created_by_id=None, created_date=None, debit_memo_id=None, id=None, invoice_id=None, updated_by_id=None, updated_date=None):  # noqa: E501
        """GETPaymentPartTypewithSuccess - a model defined in Swagger"""  # noqa: E501

        self._amount = None
        self._created_by_id = None
        self._created_date = None
        self._debit_memo_id = None
        self._id = None
        self._invoice_id = None
        self._updated_by_id = None
        self._updated_date = None
        self.discriminator = None

        if amount is not None:
            self.amount = amount
        if created_by_id is not None:
            self.created_by_id = created_by_id
        if created_date is not None:
            self.created_date = created_date
        if debit_memo_id is not None:
            self.debit_memo_id = debit_memo_id
        if id is not None:
            self.id = id
        if invoice_id is not None:
            self.invoice_id = invoice_id
        if updated_by_id is not None:
            self.updated_by_id = updated_by_id
        if updated_date is not None:
            self.updated_date = updated_date

    @property
    def amount(self):
        """Gets the amount of this GETPaymentPartTypewithSuccess.  # noqa: E501

        The amount of the payment part.   # noqa: E501

        :return: The amount of this GETPaymentPartTypewithSuccess.  # noqa: E501
        :rtype: float
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this GETPaymentPartTypewithSuccess.

        The amount of the payment part.   # noqa: E501

        :param amount: The amount of this GETPaymentPartTypewithSuccess.  # noqa: E501
        :type: float
        """

        self._amount = amount

    @property
    def created_by_id(self):
        """Gets the created_by_id of this GETPaymentPartTypewithSuccess.  # noqa: E501

        The ID of the Zuora user who created the payment part.   # noqa: E501

        :return: The created_by_id of this GETPaymentPartTypewithSuccess.  # noqa: E501
        :rtype: str
        """
        return self._created_by_id

    @created_by_id.setter
    def created_by_id(self, created_by_id):
        """Sets the created_by_id of this GETPaymentPartTypewithSuccess.

        The ID of the Zuora user who created the payment part.   # noqa: E501

        :param created_by_id: The created_by_id of this GETPaymentPartTypewithSuccess.  # noqa: E501
        :type: str
        """

        self._created_by_id = created_by_id

    @property
    def created_date(self):
        """Gets the created_date of this GETPaymentPartTypewithSuccess.  # noqa: E501

        The date and time when the payment part was created, in `yyyy-mm-dd hh:mm:ss` format. For example, 2017-03-01 15:31:10.   # noqa: E501

        :return: The created_date of this GETPaymentPartTypewithSuccess.  # noqa: E501
        :rtype: datetime
        """
        return self._created_date

    @created_date.setter
    def created_date(self, created_date):
        """Sets the created_date of this GETPaymentPartTypewithSuccess.

        The date and time when the payment part was created, in `yyyy-mm-dd hh:mm:ss` format. For example, 2017-03-01 15:31:10.   # noqa: E501

        :param created_date: The created_date of this GETPaymentPartTypewithSuccess.  # noqa: E501
        :type: datetime
        """

        self._created_date = created_date

    @property
    def debit_memo_id(self):
        """Gets the debit_memo_id of this GETPaymentPartTypewithSuccess.  # noqa: E501

        The ID of the debit memo associated with the payment part.   # noqa: E501

        :return: The debit_memo_id of this GETPaymentPartTypewithSuccess.  # noqa: E501
        :rtype: str
        """
        return self._debit_memo_id

    @debit_memo_id.setter
    def debit_memo_id(self, debit_memo_id):
        """Sets the debit_memo_id of this GETPaymentPartTypewithSuccess.

        The ID of the debit memo associated with the payment part.   # noqa: E501

        :param debit_memo_id: The debit_memo_id of this GETPaymentPartTypewithSuccess.  # noqa: E501
        :type: str
        """

        self._debit_memo_id = debit_memo_id

    @property
    def id(self):
        """Gets the id of this GETPaymentPartTypewithSuccess.  # noqa: E501

        The ID of the payment part.   # noqa: E501

        :return: The id of this GETPaymentPartTypewithSuccess.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this GETPaymentPartTypewithSuccess.

        The ID of the payment part.   # noqa: E501

        :param id: The id of this GETPaymentPartTypewithSuccess.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def invoice_id(self):
        """Gets the invoice_id of this GETPaymentPartTypewithSuccess.  # noqa: E501

        The ID of the invoice associated with the payment part.   # noqa: E501

        :return: The invoice_id of this GETPaymentPartTypewithSuccess.  # noqa: E501
        :rtype: str
        """
        return self._invoice_id

    @invoice_id.setter
    def invoice_id(self, invoice_id):
        """Sets the invoice_id of this GETPaymentPartTypewithSuccess.

        The ID of the invoice associated with the payment part.   # noqa: E501

        :param invoice_id: The invoice_id of this GETPaymentPartTypewithSuccess.  # noqa: E501
        :type: str
        """

        self._invoice_id = invoice_id

    @property
    def updated_by_id(self):
        """Gets the updated_by_id of this GETPaymentPartTypewithSuccess.  # noqa: E501

        The ID of the Zuora user who last updated the payment part.   # noqa: E501

        :return: The updated_by_id of this GETPaymentPartTypewithSuccess.  # noqa: E501
        :rtype: str
        """
        return self._updated_by_id

    @updated_by_id.setter
    def updated_by_id(self, updated_by_id):
        """Sets the updated_by_id of this GETPaymentPartTypewithSuccess.

        The ID of the Zuora user who last updated the payment part.   # noqa: E501

        :param updated_by_id: The updated_by_id of this GETPaymentPartTypewithSuccess.  # noqa: E501
        :type: str
        """

        self._updated_by_id = updated_by_id

    @property
    def updated_date(self):
        """Gets the updated_date of this GETPaymentPartTypewithSuccess.  # noqa: E501

        The date and time when the payment part was last updated, in `yyyy-mm-dd hh:mm:ss` format. For example, 2017-03-02 15:36:10.   # noqa: E501

        :return: The updated_date of this GETPaymentPartTypewithSuccess.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_date

    @updated_date.setter
    def updated_date(self, updated_date):
        """Sets the updated_date of this GETPaymentPartTypewithSuccess.

        The date and time when the payment part was last updated, in `yyyy-mm-dd hh:mm:ss` format. For example, 2017-03-02 15:36:10.   # noqa: E501

        :param updated_date: The updated_date of this GETPaymentPartTypewithSuccess.  # noqa: E501
        :type: datetime
        """

        self._updated_date = updated_date

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
        if issubclass(GETPaymentPartTypewithSuccess, dict):
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
        if not isinstance(other, GETPaymentPartTypewithSuccess):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
