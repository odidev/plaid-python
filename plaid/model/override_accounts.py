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
    from plaid.model.account_subtype import AccountSubtype
    from plaid.model.holdings_override import HoldingsOverride
    from plaid.model.inflow_model import InflowModel
    from plaid.model.investments_transactions_override import InvestmentsTransactionsOverride
    from plaid.model.liability_override import LiabilityOverride
    from plaid.model.meta import Meta
    from plaid.model.numbers import Numbers
    from plaid.model.override_account_type import OverrideAccountType
    from plaid.model.owner_override import OwnerOverride
    from plaid.model.transaction_override import TransactionOverride
    globals()['AccountSubtype'] = AccountSubtype
    globals()['HoldingsOverride'] = HoldingsOverride
    globals()['InflowModel'] = InflowModel
    globals()['InvestmentsTransactionsOverride'] = InvestmentsTransactionsOverride
    globals()['LiabilityOverride'] = LiabilityOverride
    globals()['Meta'] = Meta
    globals()['Numbers'] = Numbers
    globals()['OverrideAccountType'] = OverrideAccountType
    globals()['OwnerOverride'] = OwnerOverride
    globals()['TransactionOverride'] = TransactionOverride


class OverrideAccounts(ModelNormal):
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
            'type': (OverrideAccountType,),  # noqa: E501
            'subtype': (AccountSubtype,),  # noqa: E501
            'starting_balance': (float,),  # noqa: E501
            'force_available_balance': (float,),  # noqa: E501
            'currency': (str,),  # noqa: E501
            'meta': (Meta,),  # noqa: E501
            'numbers': (Numbers,),  # noqa: E501
            'transactions': ([TransactionOverride],),  # noqa: E501
            'identity': (OwnerOverride,),  # noqa: E501
            'liability': (LiabilityOverride,),  # noqa: E501
            'inflow_model': (InflowModel,),  # noqa: E501
            'holdings': (HoldingsOverride,),  # noqa: E501
            'investment_transactions': (InvestmentsTransactionsOverride,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'type': 'type',  # noqa: E501
        'subtype': 'subtype',  # noqa: E501
        'starting_balance': 'starting_balance',  # noqa: E501
        'force_available_balance': 'force_available_balance',  # noqa: E501
        'currency': 'currency',  # noqa: E501
        'meta': 'meta',  # noqa: E501
        'numbers': 'numbers',  # noqa: E501
        'transactions': 'transactions',  # noqa: E501
        'identity': 'identity',  # noqa: E501
        'liability': 'liability',  # noqa: E501
        'inflow_model': 'inflow_model',  # noqa: E501
        'holdings': 'holdings',  # noqa: E501
        'investment_transactions': 'investment_transactions',  # noqa: E501
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
    def __init__(self, type, subtype, starting_balance, force_available_balance, currency, meta, numbers, transactions, identity, liability, inflow_model, *args, **kwargs):  # noqa: E501
        """OverrideAccounts - a model defined in OpenAPI

        Args:
            type (OverrideAccountType):
            subtype (AccountSubtype):
            starting_balance (float): If provided, the account will start with this amount as the current balance. 
            force_available_balance (float): If provided, the account will always have this amount as its  available balance, regardless of current balance or changes in transactions over time.
            currency (str): ISO-4217 currency code. If provided, the account will be denominated in the given currency. Transactions will also be in this currency by default.
            meta (Meta):
            numbers (Numbers):
            transactions ([TransactionOverride]): Specify the list of transactions on the account.
            identity (OwnerOverride):
            liability (LiabilityOverride):
            inflow_model (InflowModel):

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
            holdings (HoldingsOverride): [optional]  # noqa: E501
            investment_transactions (InvestmentsTransactionsOverride): [optional]  # noqa: E501
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

        self.type = type
        self.subtype = subtype
        self.starting_balance = starting_balance
        self.force_available_balance = force_available_balance
        self.currency = currency
        self.meta = meta
        self.numbers = numbers
        self.transactions = transactions
        self.identity = identity
        self.liability = liability
        self.inflow_model = inflow_model
        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
