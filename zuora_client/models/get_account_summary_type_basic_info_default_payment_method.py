# coding: utf-8




import pprint
import re  # noqa: F401

import six


class GETAccountSummaryTypeBasicInfoDefaultPaymentMethod(object):
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
        'credit_card_expiration_month': 'str',
        'credit_card_expiration_year': 'str',
        'credit_card_number': 'str',
        'credit_card_type': 'str',
        'id': 'str',
        'payment_method_type': 'str'
    }

    attribute_map = {
        'credit_card_expiration_month': 'creditCardExpirationMonth',
        'credit_card_expiration_year': 'creditCardExpirationYear',
        'credit_card_number': 'creditCardNumber',
        'credit_card_type': 'creditCardType',
        'id': 'id',
        'payment_method_type': 'paymentMethodType'
    }

    def __init__(self, credit_card_expiration_month=None, credit_card_expiration_year=None, credit_card_number=None, credit_card_type=None, id=None, payment_method_type=None):  # noqa: E501
        """GETAccountSummaryTypeBasicInfoDefaultPaymentMethod - a model defined in Swagger"""  # noqa: E501

        self._credit_card_expiration_month = None
        self._credit_card_expiration_year = None
        self._credit_card_number = None
        self._credit_card_type = None
        self._id = None
        self._payment_method_type = None
        self.discriminator = None

        if credit_card_expiration_month is not None:
            self.credit_card_expiration_month = credit_card_expiration_month
        if credit_card_expiration_year is not None:
            self.credit_card_expiration_year = credit_card_expiration_year
        if credit_card_number is not None:
            self.credit_card_number = credit_card_number
        if credit_card_type is not None:
            self.credit_card_type = credit_card_type
        if id is not None:
            self.id = id
        if payment_method_type is not None:
            self.payment_method_type = payment_method_type

    @property
    def credit_card_expiration_month(self):
        """Gets the credit_card_expiration_month of this GETAccountSummaryTypeBasicInfoDefaultPaymentMethod.  # noqa: E501

        Two-digit numeric card expiration month as `mm`.   # noqa: E501

        :return: The credit_card_expiration_month of this GETAccountSummaryTypeBasicInfoDefaultPaymentMethod.  # noqa: E501
        :rtype: str
        """
        return self._credit_card_expiration_month

    @credit_card_expiration_month.setter
    def credit_card_expiration_month(self, credit_card_expiration_month):
        """Sets the credit_card_expiration_month of this GETAccountSummaryTypeBasicInfoDefaultPaymentMethod.

        Two-digit numeric card expiration month as `mm`.   # noqa: E501

        :param credit_card_expiration_month: The credit_card_expiration_month of this GETAccountSummaryTypeBasicInfoDefaultPaymentMethod.  # noqa: E501
        :type: str
        """

        self._credit_card_expiration_month = credit_card_expiration_month

    @property
    def credit_card_expiration_year(self):
        """Gets the credit_card_expiration_year of this GETAccountSummaryTypeBasicInfoDefaultPaymentMethod.  # noqa: E501

        Four-digit card expiration year as `yyyy`.   # noqa: E501

        :return: The credit_card_expiration_year of this GETAccountSummaryTypeBasicInfoDefaultPaymentMethod.  # noqa: E501
        :rtype: str
        """
        return self._credit_card_expiration_year

    @credit_card_expiration_year.setter
    def credit_card_expiration_year(self, credit_card_expiration_year):
        """Sets the credit_card_expiration_year of this GETAccountSummaryTypeBasicInfoDefaultPaymentMethod.

        Four-digit card expiration year as `yyyy`.   # noqa: E501

        :param credit_card_expiration_year: The credit_card_expiration_year of this GETAccountSummaryTypeBasicInfoDefaultPaymentMethod.  # noqa: E501
        :type: str
        """

        self._credit_card_expiration_year = credit_card_expiration_year

    @property
    def credit_card_number(self):
        """Gets the credit_card_number of this GETAccountSummaryTypeBasicInfoDefaultPaymentMethod.  # noqa: E501

        Credit card number, 16 characters or less, displayed in masked format (e.g., ************1234).   # noqa: E501

        :return: The credit_card_number of this GETAccountSummaryTypeBasicInfoDefaultPaymentMethod.  # noqa: E501
        :rtype: str
        """
        return self._credit_card_number

    @credit_card_number.setter
    def credit_card_number(self, credit_card_number):
        """Sets the credit_card_number of this GETAccountSummaryTypeBasicInfoDefaultPaymentMethod.

        Credit card number, 16 characters or less, displayed in masked format (e.g., ************1234).   # noqa: E501

        :param credit_card_number: The credit_card_number of this GETAccountSummaryTypeBasicInfoDefaultPaymentMethod.  # noqa: E501
        :type: str
        """

        self._credit_card_number = credit_card_number

    @property
    def credit_card_type(self):
        """Gets the credit_card_type of this GETAccountSummaryTypeBasicInfoDefaultPaymentMethod.  # noqa: E501

        The type of the credit card.  Possible values  include `Visa`, `MasterCard`, `AmericanExpress`, `Discover`, `JCB`, and `Diners`. For more information about credit card types supported by different payment gateways, see [Supported Payment Gateways](https://knowledgecenter.zuora.com/CB_Billing/M_Payment_Gateways/Supported_Payment_Gateways).   # noqa: E501

        :return: The credit_card_type of this GETAccountSummaryTypeBasicInfoDefaultPaymentMethod.  # noqa: E501
        :rtype: str
        """
        return self._credit_card_type

    @credit_card_type.setter
    def credit_card_type(self, credit_card_type):
        """Sets the credit_card_type of this GETAccountSummaryTypeBasicInfoDefaultPaymentMethod.

        The type of the credit card.  Possible values  include `Visa`, `MasterCard`, `AmericanExpress`, `Discover`, `JCB`, and `Diners`. For more information about credit card types supported by different payment gateways, see [Supported Payment Gateways](https://knowledgecenter.zuora.com/CB_Billing/M_Payment_Gateways/Supported_Payment_Gateways).   # noqa: E501

        :param credit_card_type: The credit_card_type of this GETAccountSummaryTypeBasicInfoDefaultPaymentMethod.  # noqa: E501
        :type: str
        """

        self._credit_card_type = credit_card_type

    @property
    def id(self):
        """Gets the id of this GETAccountSummaryTypeBasicInfoDefaultPaymentMethod.  # noqa: E501

        The ID of the credit card payment method associated with this account.   # noqa: E501

        :return: The id of this GETAccountSummaryTypeBasicInfoDefaultPaymentMethod.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this GETAccountSummaryTypeBasicInfoDefaultPaymentMethod.

        The ID of the credit card payment method associated with this account.   # noqa: E501

        :param id: The id of this GETAccountSummaryTypeBasicInfoDefaultPaymentMethod.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def payment_method_type(self):
        """Gets the payment_method_type of this GETAccountSummaryTypeBasicInfoDefaultPaymentMethod.  # noqa: E501

          # noqa: E501

        :return: The payment_method_type of this GETAccountSummaryTypeBasicInfoDefaultPaymentMethod.  # noqa: E501
        :rtype: str
        """
        return self._payment_method_type

    @payment_method_type.setter
    def payment_method_type(self, payment_method_type):
        """Sets the payment_method_type of this GETAccountSummaryTypeBasicInfoDefaultPaymentMethod.

          # noqa: E501

        :param payment_method_type: The payment_method_type of this GETAccountSummaryTypeBasicInfoDefaultPaymentMethod.  # noqa: E501
        :type: str
        """

        self._payment_method_type = payment_method_type

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
        if issubclass(GETAccountSummaryTypeBasicInfoDefaultPaymentMethod, dict):
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
        if not isinstance(other, GETAccountSummaryTypeBasicInfoDefaultPaymentMethod):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
