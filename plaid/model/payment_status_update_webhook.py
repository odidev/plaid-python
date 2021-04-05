"""
    The Plaid API

    The Plaid REST API. Please see https://plaid.com/docs/api for more details.  # noqa: E501
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from plaid.model_utils import (  # noqa: F401
    ApiTypeError,
    ModelComposed,
    ModelNormal,
    ModelSimple,
    cached_property,
    change_keys_js_to_python,
    convert_js_args_to_python_args,
    date,
    datetime,
    file_type,
    none_type,
    validate_get_composed_info,
)

def lazy_import():
    from plaid.model.error import Error
    globals()['Error'] = Error


class PaymentStatusUpdateWebhook(ModelNormal):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Attributes:
      allowed_values (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          with a capitalized key describing the allowed value and an allowed
          value. These dicts store the allowed enum values.
      attribute_map (dict): The key is attribute name
          and the value is json key in definition.
      discriminator_value_class_map (dict): A dict to go from the discriminator
          variable value to the discriminator class name.
      validations (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          that stores validations for max_length, min_length, max_items,
          min_items, exclusive_maximum, inclusive_maximum, exclusive_minimum,
          inclusive_minimum, and regex.
      additional_properties_type (tuple): A tuple of classes accepted
          as additional properties values.
    """

    allowed_values = {
        ('new_payment_status',): {
            'INPUT_NEEDED': "PAYMENT_STATUS_INPUT_NEEDED",
            'PROCESSING': "PAYMENT_STATUS_PROCESSING",
            'INITIATED': "PAYMENT_STATUS_INITIATED",
            'COMPLETED': "PAYMENT_STATUS_COMPLETED",
            'INSUFFICIENT_FUNDS': "PAYMENT_STATUS_INSUFFICIENT_FUNDS",
            'FAILED': "PAYMENT_STATUS_FAILED",
            'BLOCKED': "PAYMENT_STATUS_BLOCKED",
            'UNKNOWN': "PAYMENT_STATUS_UNKNOWN",
        },
        ('old_payment_status',): {
            'INPUT_NEEDED': "PAYMENT_STATUS_INPUT_NEEDED",
            'PROCESSING': "PAYMENT_STATUS_PROCESSING",
            'INITIATED': "PAYMENT_STATUS_INITIATED",
            'COMPLETED': "PAYMENT_STATUS_COMPLETED",
            'INSUFFICIENT_FUNDS': "PAYMENT_STATUS_INSUFFICIENT_FUNDS",
            'FAILED': "PAYMENT_STATUS_FAILED",
            'BLOCKED': "PAYMENT_STATUS_BLOCKED",
            'UNKNOWN': "PAYMENT_STATUS_UNKNOWN",
        },
    }

    validations = {
    }

    @cached_property
    def additional_properties_type():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded
        """
        lazy_import()
        return (bool, date, datetime, dict, float, int, list, str, none_type,)  # noqa: E501

    _nullable = False

    @cached_property
    def openapi_types():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded

        Returns
            openapi_types (dict): The key is attribute name
                and the value is attribute type.
        """
        lazy_import()
        return {
            'webhook_type': (str,),  # noqa: E501
            'webhook_code': (str,),  # noqa: E501
            'payment_id': (str,),  # noqa: E501
            'new_payment_status': (str,),  # noqa: E501
            'old_payment_status': (str,),  # noqa: E501
            'timestamp': (str,),  # noqa: E501
            'original_reference': (str, none_type,),  # noqa: E501
            'adjusted_reference': (str, none_type,),  # noqa: E501
            'original_start_date': (date, none_type,),  # noqa: E501
            'adjusted_start_date': (date, none_type,),  # noqa: E501
            'error': (Error,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'webhook_type': 'webhook_type',  # noqa: E501
        'webhook_code': 'webhook_code',  # noqa: E501
        'payment_id': 'payment_id',  # noqa: E501
        'new_payment_status': 'new_payment_status',  # noqa: E501
        'old_payment_status': 'old_payment_status',  # noqa: E501
        'timestamp': 'timestamp',  # noqa: E501
        'original_reference': 'original_reference',  # noqa: E501
        'adjusted_reference': 'adjusted_reference',  # noqa: E501
        'original_start_date': 'original_start_date',  # noqa: E501
        'adjusted_start_date': 'adjusted_start_date',  # noqa: E501
        'error': 'error',  # noqa: E501
    }

    _composed_schemas = {}

    required_properties = set([
        '_data_store',
        '_check_type',
        '_spec_property_naming',
        '_path_to_item',
        '_configuration',
        '_visited_composed_classes',
    ])

    @convert_js_args_to_python_args
    def __init__(self, webhook_type, webhook_code, payment_id, new_payment_status, old_payment_status, timestamp, *args, **kwargs):  # noqa: E501
        """PaymentStatusUpdateWebhook - a model defined in OpenAPI

        Args:
            webhook_type (str): `PAYMENT_INITIATION`
            webhook_code (str): `PAYMENT_STATUS_UPDATE`
            payment_id (str): The `payment_id` for the payment being updated
            new_payment_status (str): The new status of the payment.  `PAYMENT_STATUS_INPUT_NEEDED`: This is the initial state of all payments. It indicates that the payment is waiting on user input to continue processing. A payment may re-enter this state later on if further input is needed.  `PAYMENT_STATUS_PROCESSING`: The payment is currently being processed. The payment will automatically exit this state when processing is complete.  `PAYMENT_STATUS_INITIATED`: The payment has been successfully initiated and is considered complete.  `PAYMENT_STATUS_COMPLETED`: Indicates that the standing order has been successfully established. This state is only used for standing orders.  `PAYMENT_STATUS_INSUFFICIENT_FUNDS`: The payment has failed due to insufficient funds.  `PAYMENT_STATUS_FAILED`: The payment has failed to be initiated. This error is retryable once the root cause is resolved.  `PAYMENT_STATUS_BLOCKED`: The payment has been blocked. This is a retryable error.  `PAYMENT_STATUS_UNKNOWN`: The payment status is unknown.
            old_payment_status (str): The previous status of the payment.  `PAYMENT_STATUS_INPUT_NEEDED`: This is the initial state of all payments. It indicates that the payment is waiting on user input to continue processing. A payment may re-enter this state later on if further input is needed.  `PAYMENT_STATUS_PROCESSING`: The payment is currently being processed. The payment will automatically exit this state when processing is complete.  `PAYMENT_STATUS_INITIATED`: The payment has been successfully initiated and is considered complete.  `PAYMENT_STATUS_COMPLETED`: Indicates that the standing order has been successfully established. This state is only used for standing orders.  `PAYMENT_STATUS_INSUFFICIENT_FUNDS`: The payment has failed due to insufficient funds.  `PAYMENT_STATUS_FAILED`: The payment has failed to be initiated. This error is retryable once the root cause is resolved.  `PAYMENT_STATUS_BLOCKED`: The payment has been blocked. This is a retryable error.  `PAYMENT_STATUS_UNKNOWN`: The payment status is unknown.
            timestamp (str): The timestamp of the update, in ISO 8601 format, e.g. `\"2017-09-14T14:42:19.350Z\"`

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            original_reference (str, none_type): The original value of the reference when creating the payment.. [optional]  # noqa: E501
            adjusted_reference (str, none_type): The value of the reference sent to the bank after adjustment to pass bank validation rules.. [optional]  # noqa: E501
            original_start_date (date, none_type): The original value of the `start_date` provided during the creation of a standing order. If the payment is not a standing order, this field will be `null`.. [optional]  # noqa: E501
            adjusted_start_date (date, none_type): The start date sent to the bank after adjusting for holidays or weekends.  Will be provided in ISO 8601 format (YYYY-MM-DD). If the start date did not require adjustment, or if the payment is not a standing order, this field will be `null`.. [optional]  # noqa: E501
            error (Error): [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        if args:
            raise ApiTypeError(
                "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                    args,
                    self.__class__.__name__,
                ),
                path_to_item=_path_to_item,
                valid_classes=(self.__class__,),
            )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        self.webhook_type = webhook_type
        self.webhook_code = webhook_code
        self.payment_id = payment_id
        self.new_payment_status = new_payment_status
        self.old_payment_status = old_payment_status
        self.timestamp = timestamp
        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
