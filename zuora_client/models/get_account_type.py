# coding: utf-8




import pprint
import re  # noqa: F401

import six

from zuora_client.models.get_account_summary_type_tax_info import GETAccountSummaryTypeTaxInfo  # noqa: F401,E501
from zuora_client.models.get_account_type_basic_info import GETAccountTypeBasicInfo  # noqa: F401,E501
from zuora_client.models.get_account_type_bill_to_contact import GETAccountTypeBillToContact  # noqa: F401,E501
from zuora_client.models.get_account_type_billing_and_payment import GETAccountTypeBillingAndPayment  # noqa: F401,E501
from zuora_client.models.get_account_type_metrics import GETAccountTypeMetrics  # noqa: F401,E501
from zuora_client.models.get_account_type_sold_to_contact import GETAccountTypeSoldToContact  # noqa: F401,E501


class GETAccountType(object):
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
        'basic_info': 'GETAccountTypeBasicInfo',
        'bill_to_contact': 'GETAccountTypeBillToContact',
        'billing_and_payment': 'GETAccountTypeBillingAndPayment',
        'metrics': 'GETAccountTypeMetrics',
        'sold_to_contact': 'GETAccountTypeSoldToContact',
        'success': 'bool',
        'tax_info': 'GETAccountSummaryTypeTaxInfo'
    }

    attribute_map = {
        'basic_info': 'basicInfo',
        'bill_to_contact': 'billToContact',
        'billing_and_payment': 'billingAndPayment',
        'metrics': 'metrics',
        'sold_to_contact': 'soldToContact',
        'success': 'success',
        'tax_info': 'taxInfo'
    }

    def __init__(self, basic_info=None, bill_to_contact=None, billing_and_payment=None, metrics=None, sold_to_contact=None, success=None, tax_info=None):  # noqa: E501
        """GETAccountType - a model defined in Swagger"""  # noqa: E501

        self._basic_info = None
        self._bill_to_contact = None
        self._billing_and_payment = None
        self._metrics = None
        self._sold_to_contact = None
        self._success = None
        self._tax_info = None
        self.discriminator = None

        if basic_info is not None:
            self.basic_info = basic_info
        if bill_to_contact is not None:
            self.bill_to_contact = bill_to_contact
        if billing_and_payment is not None:
            self.billing_and_payment = billing_and_payment
        if metrics is not None:
            self.metrics = metrics
        if sold_to_contact is not None:
            self.sold_to_contact = sold_to_contact
        if success is not None:
            self.success = success
        if tax_info is not None:
            self.tax_info = tax_info

    @property
    def basic_info(self):
        """Gets the basic_info of this GETAccountType.  # noqa: E501


        :return: The basic_info of this GETAccountType.  # noqa: E501
        :rtype: GETAccountTypeBasicInfo
        """
        return self._basic_info

    @basic_info.setter
    def basic_info(self, basic_info):
        """Sets the basic_info of this GETAccountType.


        :param basic_info: The basic_info of this GETAccountType.  # noqa: E501
        :type: GETAccountTypeBasicInfo
        """

        self._basic_info = basic_info

    @property
    def bill_to_contact(self):
        """Gets the bill_to_contact of this GETAccountType.  # noqa: E501


        :return: The bill_to_contact of this GETAccountType.  # noqa: E501
        :rtype: GETAccountTypeBillToContact
        """
        return self._bill_to_contact

    @bill_to_contact.setter
    def bill_to_contact(self, bill_to_contact):
        """Sets the bill_to_contact of this GETAccountType.


        :param bill_to_contact: The bill_to_contact of this GETAccountType.  # noqa: E501
        :type: GETAccountTypeBillToContact
        """

        self._bill_to_contact = bill_to_contact

    @property
    def billing_and_payment(self):
        """Gets the billing_and_payment of this GETAccountType.  # noqa: E501


        :return: The billing_and_payment of this GETAccountType.  # noqa: E501
        :rtype: GETAccountTypeBillingAndPayment
        """
        return self._billing_and_payment

    @billing_and_payment.setter
    def billing_and_payment(self, billing_and_payment):
        """Sets the billing_and_payment of this GETAccountType.


        :param billing_and_payment: The billing_and_payment of this GETAccountType.  # noqa: E501
        :type: GETAccountTypeBillingAndPayment
        """

        self._billing_and_payment = billing_and_payment

    @property
    def metrics(self):
        """Gets the metrics of this GETAccountType.  # noqa: E501


        :return: The metrics of this GETAccountType.  # noqa: E501
        :rtype: GETAccountTypeMetrics
        """
        return self._metrics

    @metrics.setter
    def metrics(self, metrics):
        """Sets the metrics of this GETAccountType.


        :param metrics: The metrics of this GETAccountType.  # noqa: E501
        :type: GETAccountTypeMetrics
        """

        self._metrics = metrics

    @property
    def sold_to_contact(self):
        """Gets the sold_to_contact of this GETAccountType.  # noqa: E501


        :return: The sold_to_contact of this GETAccountType.  # noqa: E501
        :rtype: GETAccountTypeSoldToContact
        """
        return self._sold_to_contact

    @sold_to_contact.setter
    def sold_to_contact(self, sold_to_contact):
        """Sets the sold_to_contact of this GETAccountType.


        :param sold_to_contact: The sold_to_contact of this GETAccountType.  # noqa: E501
        :type: GETAccountTypeSoldToContact
        """

        self._sold_to_contact = sold_to_contact

    @property
    def success(self):
        """Gets the success of this GETAccountType.  # noqa: E501

        Returns `true` if the request was processed successfully.   # noqa: E501

        :return: The success of this GETAccountType.  # noqa: E501
        :rtype: bool
        """
        return self._success

    @success.setter
    def success(self, success):
        """Sets the success of this GETAccountType.

        Returns `true` if the request was processed successfully.   # noqa: E501

        :param success: The success of this GETAccountType.  # noqa: E501
        :type: bool
        """

        self._success = success

    @property
    def tax_info(self):
        """Gets the tax_info of this GETAccountType.  # noqa: E501


        :return: The tax_info of this GETAccountType.  # noqa: E501
        :rtype: GETAccountSummaryTypeTaxInfo
        """
        return self._tax_info

    @tax_info.setter
    def tax_info(self, tax_info):
        """Sets the tax_info of this GETAccountType.


        :param tax_info: The tax_info of this GETAccountType.  # noqa: E501
        :type: GETAccountSummaryTypeTaxInfo
        """

        self._tax_info = tax_info

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
        if issubclass(GETAccountType, dict):
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
        if not isinstance(other, GETAccountType):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
