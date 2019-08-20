# coding: utf-8




import pprint
import re  # noqa: F401

import six

from zuora_client.models.put_order_patch_request_type_order_actions import PUTOrderPatchRequestTypeOrderActions  # noqa: F401,E501


class PUTOrderPatchRequestTypeSubscriptions(object):
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
        'order_actions': 'list[PUTOrderPatchRequestTypeOrderActions]',
        'subscription_number': 'str'
    }

    attribute_map = {
        'order_actions': 'orderActions',
        'subscription_number': 'subscriptionNumber'
    }

    def __init__(self, order_actions=None, subscription_number=None):  # noqa: E501
        """PUTOrderPatchRequestTypeSubscriptions - a model defined in Swagger"""  # noqa: E501

        self._order_actions = None
        self._subscription_number = None
        self.discriminator = None

        if order_actions is not None:
            self.order_actions = order_actions
        if subscription_number is not None:
            self.subscription_number = subscription_number

    @property
    def order_actions(self):
        """Gets the order_actions of this PUTOrderPatchRequestTypeSubscriptions.  # noqa: E501


        :return: The order_actions of this PUTOrderPatchRequestTypeSubscriptions.  # noqa: E501
        :rtype: list[PUTOrderPatchRequestTypeOrderActions]
        """
        return self._order_actions

    @order_actions.setter
    def order_actions(self, order_actions):
        """Sets the order_actions of this PUTOrderPatchRequestTypeSubscriptions.


        :param order_actions: The order_actions of this PUTOrderPatchRequestTypeSubscriptions.  # noqa: E501
        :type: list[PUTOrderPatchRequestTypeOrderActions]
        """

        self._order_actions = order_actions

    @property
    def subscription_number(self):
        """Gets the subscription_number of this PUTOrderPatchRequestTypeSubscriptions.  # noqa: E501


        :return: The subscription_number of this PUTOrderPatchRequestTypeSubscriptions.  # noqa: E501
        :rtype: str
        """
        return self._subscription_number

    @subscription_number.setter
    def subscription_number(self, subscription_number):
        """Sets the subscription_number of this PUTOrderPatchRequestTypeSubscriptions.


        :param subscription_number: The subscription_number of this PUTOrderPatchRequestTypeSubscriptions.  # noqa: E501
        :type: str
        """

        self._subscription_number = subscription_number

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
        if issubclass(PUTOrderPatchRequestTypeSubscriptions, dict):
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
        if not isinstance(other, PUTOrderPatchRequestTypeSubscriptions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other