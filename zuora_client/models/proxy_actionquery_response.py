# coding: utf-8




import pprint
import re  # noqa: F401

import six

from zuora_client.models.z_object import ZObject  # noqa: F401,E501


class ProxyActionqueryResponse(object):
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
        'done': 'bool',
        'query_locator': 'str',
        'records': 'list[ZObject]',
        'size': 'int'
    }

    attribute_map = {
        'done': 'done',
        'query_locator': 'queryLocator',
        'records': 'records',
        'size': 'size'
    }

    def __init__(self, done=None, query_locator=None, records=None, size=None):  # noqa: E501
        """ProxyActionqueryResponse - a model defined in Swagger"""  # noqa: E501

        self._done = None
        self._query_locator = None
        self._records = None
        self._size = None
        self.discriminator = None

        if done is not None:
            self.done = done
        if query_locator is not None:
            self.query_locator = query_locator
        if records is not None:
            self.records = records
        if size is not None:
            self.size = size

    @property
    def done(self):
        """Gets the done of this ProxyActionqueryResponse.  # noqa: E501

          # noqa: E501

        :return: The done of this ProxyActionqueryResponse.  # noqa: E501
        :rtype: bool
        """
        return self._done

    @done.setter
    def done(self, done):
        """Sets the done of this ProxyActionqueryResponse.

          # noqa: E501

        :param done: The done of this ProxyActionqueryResponse.  # noqa: E501
        :type: bool
        """

        self._done = done

    @property
    def query_locator(self):
        """Gets the query_locator of this ProxyActionqueryResponse.  # noqa: E501

          # noqa: E501

        :return: The query_locator of this ProxyActionqueryResponse.  # noqa: E501
        :rtype: str
        """
        return self._query_locator

    @query_locator.setter
    def query_locator(self, query_locator):
        """Sets the query_locator of this ProxyActionqueryResponse.

          # noqa: E501

        :param query_locator: The query_locator of this ProxyActionqueryResponse.  # noqa: E501
        :type: str
        """

        self._query_locator = query_locator

    @property
    def records(self):
        """Gets the records of this ProxyActionqueryResponse.  # noqa: E501

          # noqa: E501

        :return: The records of this ProxyActionqueryResponse.  # noqa: E501
        :rtype: list[ZObject]
        """
        return self._records

    @records.setter
    def records(self, records):
        """Sets the records of this ProxyActionqueryResponse.

          # noqa: E501

        :param records: The records of this ProxyActionqueryResponse.  # noqa: E501
        :type: list[ZObject]
        """

        self._records = records

    @property
    def size(self):
        """Gets the size of this ProxyActionqueryResponse.  # noqa: E501

          # noqa: E501

        :return: The size of this ProxyActionqueryResponse.  # noqa: E501
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this ProxyActionqueryResponse.

          # noqa: E501

        :param size: The size of this ProxyActionqueryResponse.  # noqa: E501
        :type: int
        """

        self._size = size

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
        if issubclass(ProxyActionqueryResponse, dict):
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
        if not isinstance(other, ProxyActionqueryResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
