# coding: utf-8




import pprint
import re  # noqa: F401

import six

from zuora_client.models.get_product_rate_plan_charge_pricing_tier_type import GETProductRatePlanChargePricingTierType  # noqa: F401,E501


class GETProductRatePlanChargePricingType(object):
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
        'currency': 'str',
        'discount_amount': 'str',
        'discount_percentage': 'str',
        'included_units': 'str',
        'overage_price': 'str',
        'price': 'str',
        'tiers': 'list[GETProductRatePlanChargePricingTierType]'
    }

    attribute_map = {
        'currency': 'currency',
        'discount_amount': 'discountAmount',
        'discount_percentage': 'discountPercentage',
        'included_units': 'includedUnits',
        'overage_price': 'overagePrice',
        'price': 'price',
        'tiers': 'tiers'
    }

    def __init__(self, currency=None, discount_amount=None, discount_percentage=None, included_units=None, overage_price=None, price=None, tiers=None):  # noqa: E501
        """GETProductRatePlanChargePricingType - a model defined in Swagger"""  # noqa: E501

        self._currency = None
        self._discount_amount = None
        self._discount_percentage = None
        self._included_units = None
        self._overage_price = None
        self._price = None
        self._tiers = None
        self.discriminator = None

        if currency is not None:
            self.currency = currency
        if discount_amount is not None:
            self.discount_amount = discount_amount
        if discount_percentage is not None:
            self.discount_percentage = discount_percentage
        if included_units is not None:
            self.included_units = included_units
        if overage_price is not None:
            self.overage_price = overage_price
        if price is not None:
            self.price = price
        if tiers is not None:
            self.tiers = tiers

    @property
    def currency(self):
        """Gets the currency of this GETProductRatePlanChargePricingType.  # noqa: E501

        Currency used by the charge model. For example: USD or EUR   # noqa: E501

        :return: The currency of this GETProductRatePlanChargePricingType.  # noqa: E501
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this GETProductRatePlanChargePricingType.

        Currency used by the charge model. For example: USD or EUR   # noqa: E501

        :param currency: The currency of this GETProductRatePlanChargePricingType.  # noqa: E501
        :type: str
        """

        self._currency = currency

    @property
    def discount_amount(self):
        """Gets the discount_amount of this GETProductRatePlanChargePricingType.  # noqa: E501

        Value subtracted from price in currency specified. Used only when the charge model is DiscountFixedAmount.   # noqa: E501

        :return: The discount_amount of this GETProductRatePlanChargePricingType.  # noqa: E501
        :rtype: str
        """
        return self._discount_amount

    @discount_amount.setter
    def discount_amount(self, discount_amount):
        """Sets the discount_amount of this GETProductRatePlanChargePricingType.

        Value subtracted from price in currency specified. Used only when the charge model is DiscountFixedAmount.   # noqa: E501

        :param discount_amount: The discount_amount of this GETProductRatePlanChargePricingType.  # noqa: E501
        :type: str
        """

        self._discount_amount = discount_amount

    @property
    def discount_percentage(self):
        """Gets the discount_percentage of this GETProductRatePlanChargePricingType.  # noqa: E501

        Percent discount applied to the price. Used only when the charge model is DiscountPercentage.   # noqa: E501

        :return: The discount_percentage of this GETProductRatePlanChargePricingType.  # noqa: E501
        :rtype: str
        """
        return self._discount_percentage

    @discount_percentage.setter
    def discount_percentage(self, discount_percentage):
        """Sets the discount_percentage of this GETProductRatePlanChargePricingType.

        Percent discount applied to the price. Used only when the charge model is DiscountPercentage.   # noqa: E501

        :param discount_percentage: The discount_percentage of this GETProductRatePlanChargePricingType.  # noqa: E501
        :type: str
        """

        self._discount_percentage = discount_percentage

    @property
    def included_units(self):
        """Gets the included_units of this GETProductRatePlanChargePricingType.  # noqa: E501

        Specifies the number of units in the base set of units when the charge model is Overage.   # noqa: E501

        :return: The included_units of this GETProductRatePlanChargePricingType.  # noqa: E501
        :rtype: str
        """
        return self._included_units

    @included_units.setter
    def included_units(self, included_units):
        """Sets the included_units of this GETProductRatePlanChargePricingType.

        Specifies the number of units in the base set of units when the charge model is Overage.   # noqa: E501

        :param included_units: The included_units of this GETProductRatePlanChargePricingType.  # noqa: E501
        :type: str
        """

        self._included_units = included_units

    @property
    def overage_price(self):
        """Gets the overage_price of this GETProductRatePlanChargePricingType.  # noqa: E501

        Price per unit when base set of units is exceeded. Used only when charge model is Overage or Tiered with Overage.   # noqa: E501

        :return: The overage_price of this GETProductRatePlanChargePricingType.  # noqa: E501
        :rtype: str
        """
        return self._overage_price

    @overage_price.setter
    def overage_price(self, overage_price):
        """Sets the overage_price of this GETProductRatePlanChargePricingType.

        Price per unit when base set of units is exceeded. Used only when charge model is Overage or Tiered with Overage.   # noqa: E501

        :param overage_price: The overage_price of this GETProductRatePlanChargePricingType.  # noqa: E501
        :type: str
        """

        self._overage_price = overage_price

    @property
    def price(self):
        """Gets the price of this GETProductRatePlanChargePricingType.  # noqa: E501

        The decimal value that applies when the charge model is not tiered   # noqa: E501

        :return: The price of this GETProductRatePlanChargePricingType.  # noqa: E501
        :rtype: str
        """
        return self._price

    @price.setter
    def price(self, price):
        """Sets the price of this GETProductRatePlanChargePricingType.

        The decimal value that applies when the charge model is not tiered   # noqa: E501

        :param price: The price of this GETProductRatePlanChargePricingType.  # noqa: E501
        :type: str
        """

        self._price = price

    @property
    def tiers(self):
        """Gets the tiers of this GETProductRatePlanChargePricingType.  # noqa: E501

        Container for one or many defined tier ranges with distinct pricing.  Applies when model is `Tiered`, `TieredWithOverage`, or `Volume`   # noqa: E501

        :return: The tiers of this GETProductRatePlanChargePricingType.  # noqa: E501
        :rtype: list[GETProductRatePlanChargePricingTierType]
        """
        return self._tiers

    @tiers.setter
    def tiers(self, tiers):
        """Sets the tiers of this GETProductRatePlanChargePricingType.

        Container for one or many defined tier ranges with distinct pricing.  Applies when model is `Tiered`, `TieredWithOverage`, or `Volume`   # noqa: E501

        :param tiers: The tiers of this GETProductRatePlanChargePricingType.  # noqa: E501
        :type: list[GETProductRatePlanChargePricingTierType]
        """

        self._tiers = tiers

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
        if issubclass(GETProductRatePlanChargePricingType, dict):
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
        if not isinstance(other, GETProductRatePlanChargePricingType):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other