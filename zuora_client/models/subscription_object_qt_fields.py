# coding: utf-8




import pprint
import re  # noqa: F401

import six


class SubscriptionObjectQTFields(object):
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
        'cpq_bundle_json_id__qt': 'str',
        'opportunity_close_date__qt': 'date',
        'opportunity_name__qt': 'str',
        'quote_business_type__qt': 'str',
        'quote_number__qt': 'str',
        'quote_type__qt': 'str'
    }

    attribute_map = {
        'cpq_bundle_json_id__qt': 'CpqBundleJsonId__QT',
        'opportunity_close_date__qt': 'OpportunityCloseDate__QT',
        'opportunity_name__qt': 'OpportunityName__QT',
        'quote_business_type__qt': 'QuoteBusinessType__QT',
        'quote_number__qt': 'QuoteNumber__QT',
        'quote_type__qt': 'QuoteType__QT'
    }

    def __init__(self, cpq_bundle_json_id__qt=None, opportunity_close_date__qt=None, opportunity_name__qt=None, quote_business_type__qt=None, quote_number__qt=None, quote_type__qt=None):  # noqa: E501
        """SubscriptionObjectQTFields - a model defined in Swagger"""  # noqa: E501

        self._cpq_bundle_json_id__qt = None
        self._opportunity_close_date__qt = None
        self._opportunity_name__qt = None
        self._quote_business_type__qt = None
        self._quote_number__qt = None
        self._quote_type__qt = None
        self.discriminator = None

        if cpq_bundle_json_id__qt is not None:
            self.cpq_bundle_json_id__qt = cpq_bundle_json_id__qt
        if opportunity_close_date__qt is not None:
            self.opportunity_close_date__qt = opportunity_close_date__qt
        if opportunity_name__qt is not None:
            self.opportunity_name__qt = opportunity_name__qt
        if quote_business_type__qt is not None:
            self.quote_business_type__qt = quote_business_type__qt
        if quote_number__qt is not None:
            self.quote_number__qt = quote_number__qt
        if quote_type__qt is not None:
            self.quote_type__qt = quote_type__qt

    @property
    def cpq_bundle_json_id__qt(self):
        """Gets the cpq_bundle_json_id__qt of this SubscriptionObjectQTFields.  # noqa: E501

        The Bundle product structures from Zuora Quotes if you utilize Bundling in Salesforce. Do not change the value in this field.   # noqa: E501

        :return: The cpq_bundle_json_id__qt of this SubscriptionObjectQTFields.  # noqa: E501
        :rtype: str
        """
        return self._cpq_bundle_json_id__qt

    @cpq_bundle_json_id__qt.setter
    def cpq_bundle_json_id__qt(self, cpq_bundle_json_id__qt):
        """Sets the cpq_bundle_json_id__qt of this SubscriptionObjectQTFields.

        The Bundle product structures from Zuora Quotes if you utilize Bundling in Salesforce. Do not change the value in this field.   # noqa: E501

        :param cpq_bundle_json_id__qt: The cpq_bundle_json_id__qt of this SubscriptionObjectQTFields.  # noqa: E501
        :type: str
        """
        if cpq_bundle_json_id__qt is not None and len(cpq_bundle_json_id__qt) > 32:
            raise ValueError("Invalid value for `cpq_bundle_json_id__qt`, length must be less than or equal to `32`")  # noqa: E501

        self._cpq_bundle_json_id__qt = cpq_bundle_json_id__qt

    @property
    def opportunity_close_date__qt(self):
        """Gets the opportunity_close_date__qt of this SubscriptionObjectQTFields.  # noqa: E501

        The closing date of the Opportunity. This field is used in Zuora data sources to report on Subscription metrics. If the subscription originated from Zuora Quotes, the value is populated with the value from Zuora Quotes.   # noqa: E501

        :return: The opportunity_close_date__qt of this SubscriptionObjectQTFields.  # noqa: E501
        :rtype: date
        """
        return self._opportunity_close_date__qt

    @opportunity_close_date__qt.setter
    def opportunity_close_date__qt(self, opportunity_close_date__qt):
        """Sets the opportunity_close_date__qt of this SubscriptionObjectQTFields.

        The closing date of the Opportunity. This field is used in Zuora data sources to report on Subscription metrics. If the subscription originated from Zuora Quotes, the value is populated with the value from Zuora Quotes.   # noqa: E501

        :param opportunity_close_date__qt: The opportunity_close_date__qt of this SubscriptionObjectQTFields.  # noqa: E501
        :type: date
        """

        self._opportunity_close_date__qt = opportunity_close_date__qt

    @property
    def opportunity_name__qt(self):
        """Gets the opportunity_name__qt of this SubscriptionObjectQTFields.  # noqa: E501

        The unique identifier of the Opportunity. This field is used in Zuora data sources to report on Subscription metrics. If the subscription originated from Zuora Quotes, the value is populated with the value from Zuora Quotes.   # noqa: E501

        :return: The opportunity_name__qt of this SubscriptionObjectQTFields.  # noqa: E501
        :rtype: str
        """
        return self._opportunity_name__qt

    @opportunity_name__qt.setter
    def opportunity_name__qt(self, opportunity_name__qt):
        """Sets the opportunity_name__qt of this SubscriptionObjectQTFields.

        The unique identifier of the Opportunity. This field is used in Zuora data sources to report on Subscription metrics. If the subscription originated from Zuora Quotes, the value is populated with the value from Zuora Quotes.   # noqa: E501

        :param opportunity_name__qt: The opportunity_name__qt of this SubscriptionObjectQTFields.  # noqa: E501
        :type: str
        """
        if opportunity_name__qt is not None and len(opportunity_name__qt) > 100:
            raise ValueError("Invalid value for `opportunity_name__qt`, length must be less than or equal to `100`")  # noqa: E501

        self._opportunity_name__qt = opportunity_name__qt

    @property
    def quote_business_type__qt(self):
        """Gets the quote_business_type__qt of this SubscriptionObjectQTFields.  # noqa: E501

        The specific identifier for the type of business transaction the Quote represents such as New, Upsell, Downsell, Renewal or Churn. This field is used in Zuora data sources to report on Subscription metrics. If the subscription originated from Zuora Quotes, the value is populated with the value from Zuora Quotes.   # noqa: E501

        :return: The quote_business_type__qt of this SubscriptionObjectQTFields.  # noqa: E501
        :rtype: str
        """
        return self._quote_business_type__qt

    @quote_business_type__qt.setter
    def quote_business_type__qt(self, quote_business_type__qt):
        """Sets the quote_business_type__qt of this SubscriptionObjectQTFields.

        The specific identifier for the type of business transaction the Quote represents such as New, Upsell, Downsell, Renewal or Churn. This field is used in Zuora data sources to report on Subscription metrics. If the subscription originated from Zuora Quotes, the value is populated with the value from Zuora Quotes.   # noqa: E501

        :param quote_business_type__qt: The quote_business_type__qt of this SubscriptionObjectQTFields.  # noqa: E501
        :type: str
        """
        if quote_business_type__qt is not None and len(quote_business_type__qt) > 32:
            raise ValueError("Invalid value for `quote_business_type__qt`, length must be less than or equal to `32`")  # noqa: E501

        self._quote_business_type__qt = quote_business_type__qt

    @property
    def quote_number__qt(self):
        """Gets the quote_number__qt of this SubscriptionObjectQTFields.  # noqa: E501

        The unique identifier of the Quote. This field is used in Zuora data sources to report on Subscription metrics. If the subscription originated from Zuora Quotes, the value is populated with the value from Zuora Quotes.   # noqa: E501

        :return: The quote_number__qt of this SubscriptionObjectQTFields.  # noqa: E501
        :rtype: str
        """
        return self._quote_number__qt

    @quote_number__qt.setter
    def quote_number__qt(self, quote_number__qt):
        """Sets the quote_number__qt of this SubscriptionObjectQTFields.

        The unique identifier of the Quote. This field is used in Zuora data sources to report on Subscription metrics. If the subscription originated from Zuora Quotes, the value is populated with the value from Zuora Quotes.   # noqa: E501

        :param quote_number__qt: The quote_number__qt of this SubscriptionObjectQTFields.  # noqa: E501
        :type: str
        """
        if quote_number__qt is not None and len(quote_number__qt) > 32:
            raise ValueError("Invalid value for `quote_number__qt`, length must be less than or equal to `32`")  # noqa: E501

        self._quote_number__qt = quote_number__qt

    @property
    def quote_type__qt(self):
        """Gets the quote_type__qt of this SubscriptionObjectQTFields.  # noqa: E501

        The Quote type that represents the subscription lifecycle stage such as New, Amendment, Renew or Cancel. This field is used in Zuora data sources to report on Subscription metrics. If the subscription originated from Zuora Quotes, the value is populated with the value from Zuora Quotes.   # noqa: E501

        :return: The quote_type__qt of this SubscriptionObjectQTFields.  # noqa: E501
        :rtype: str
        """
        return self._quote_type__qt

    @quote_type__qt.setter
    def quote_type__qt(self, quote_type__qt):
        """Sets the quote_type__qt of this SubscriptionObjectQTFields.

        The Quote type that represents the subscription lifecycle stage such as New, Amendment, Renew or Cancel. This field is used in Zuora data sources to report on Subscription metrics. If the subscription originated from Zuora Quotes, the value is populated with the value from Zuora Quotes.   # noqa: E501

        :param quote_type__qt: The quote_type__qt of this SubscriptionObjectQTFields.  # noqa: E501
        :type: str
        """
        if quote_type__qt is not None and len(quote_type__qt) > 32:
            raise ValueError("Invalid value for `quote_type__qt`, length must be less than or equal to `32`")  # noqa: E501

        self._quote_type__qt = quote_type__qt

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
        if issubclass(SubscriptionObjectQTFields, dict):
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
        if not isinstance(other, SubscriptionObjectQTFields):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other