# coding: utf-8




import pprint
import re  # noqa: F401

import six


class GETDMTaxItemTypeFinanceInformation(object):
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
        'sales_tax_payable_accounting_code': 'str',
        'sales_tax_payable_accounting_code_type': 'str'
    }

    attribute_map = {
        'sales_tax_payable_accounting_code': 'salesTaxPayableAccountingCode',
        'sales_tax_payable_accounting_code_type': 'salesTaxPayableAccountingCodeType'
    }

    def __init__(self, sales_tax_payable_accounting_code=None, sales_tax_payable_accounting_code_type=None):  # noqa: E501
        """GETDMTaxItemTypeFinanceInformation - a model defined in Swagger"""  # noqa: E501

        self._sales_tax_payable_accounting_code = None
        self._sales_tax_payable_accounting_code_type = None
        self.discriminator = None

        if sales_tax_payable_accounting_code is not None:
            self.sales_tax_payable_accounting_code = sales_tax_payable_accounting_code
        if sales_tax_payable_accounting_code_type is not None:
            self.sales_tax_payable_accounting_code_type = sales_tax_payable_accounting_code_type

    @property
    def sales_tax_payable_accounting_code(self):
        """Gets the sales_tax_payable_accounting_code of this GETDMTaxItemTypeFinanceInformation.  # noqa: E501

        The accounting code for the sales taxes payable.   # noqa: E501

        :return: The sales_tax_payable_accounting_code of this GETDMTaxItemTypeFinanceInformation.  # noqa: E501
        :rtype: str
        """
        return self._sales_tax_payable_accounting_code

    @sales_tax_payable_accounting_code.setter
    def sales_tax_payable_accounting_code(self, sales_tax_payable_accounting_code):
        """Sets the sales_tax_payable_accounting_code of this GETDMTaxItemTypeFinanceInformation.

        The accounting code for the sales taxes payable.   # noqa: E501

        :param sales_tax_payable_accounting_code: The sales_tax_payable_accounting_code of this GETDMTaxItemTypeFinanceInformation.  # noqa: E501
        :type: str
        """

        self._sales_tax_payable_accounting_code = sales_tax_payable_accounting_code

    @property
    def sales_tax_payable_accounting_code_type(self):
        """Gets the sales_tax_payable_accounting_code_type of this GETDMTaxItemTypeFinanceInformation.  # noqa: E501

        The type of the accounting code for the sales taxes payable.   # noqa: E501

        :return: The sales_tax_payable_accounting_code_type of this GETDMTaxItemTypeFinanceInformation.  # noqa: E501
        :rtype: str
        """
        return self._sales_tax_payable_accounting_code_type

    @sales_tax_payable_accounting_code_type.setter
    def sales_tax_payable_accounting_code_type(self, sales_tax_payable_accounting_code_type):
        """Sets the sales_tax_payable_accounting_code_type of this GETDMTaxItemTypeFinanceInformation.

        The type of the accounting code for the sales taxes payable.   # noqa: E501

        :param sales_tax_payable_accounting_code_type: The sales_tax_payable_accounting_code_type of this GETDMTaxItemTypeFinanceInformation.  # noqa: E501
        :type: str
        """

        self._sales_tax_payable_accounting_code_type = sales_tax_payable_accounting_code_type

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
        if issubclass(GETDMTaxItemTypeFinanceInformation, dict):
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
        if not isinstance(other, GETDMTaxItemTypeFinanceInformation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
