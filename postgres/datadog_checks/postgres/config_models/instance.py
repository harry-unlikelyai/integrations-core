# (C) Datadog, Inc. 2021-present
# All rights reserved
# Licensed under a 3-clause BSD style license (see LICENSE)

# This file is autogenerated.
# To change this file you should edit assets/configuration/spec.yaml and then run the following commands:
#     ddev -x validate config -s <INTEGRATION_NAME>
#     ddev -x validate models -s <INTEGRATION_NAME>

from __future__ import annotations

from types import MappingProxyType
from typing import Any, Optional, Union

from pydantic import BaseModel, ConfigDict, field_validator, model_validator

from datadog_checks.base.utils.functions import identity
from datadog_checks.base.utils.models import validation

from . import defaults, validators


class Aws(BaseModel):
    model_config = ConfigDict(
        arbitrary_types_allowed=True,
        frozen=True,
    )
    instance_endpoint: Optional[str] = None
    region: Optional[str] = None


class Azure(BaseModel):
    model_config = ConfigDict(
        arbitrary_types_allowed=True,
        frozen=True,
    )
    deployment_type: Optional[str] = None
    fully_qualified_domain_name: Optional[str] = None


class CollectSchemas(BaseModel):
    model_config = ConfigDict(
        arbitrary_types_allowed=True,
        frozen=True,
    )
    collection_interval: Optional[float] = None
    enabled: Optional[bool] = None
    max_columns: Optional[float] = None
    max_tables: Optional[float] = None


class CollectSettings(BaseModel):
    model_config = ConfigDict(
        arbitrary_types_allowed=True,
        frozen=True,
    )
    collection_interval: Optional[float] = None
    enabled: Optional[bool] = None


class DatabaseAutodiscovery(BaseModel):
    model_config = ConfigDict(
        arbitrary_types_allowed=True,
        frozen=True,
    )
    enabled: Optional[bool] = None
    exclude: Optional[tuple[str, ...]] = None
    include: Optional[tuple[str, ...]] = None
    max_databases: Optional[int] = None
    refresh: Optional[int] = None


class Gcp(BaseModel):
    model_config = ConfigDict(
        arbitrary_types_allowed=True,
        frozen=True,
    )
    instance_id: Optional[str] = None
    project_id: Optional[str] = None


class ManagedIdentity(BaseModel):
    model_config = ConfigDict(
        arbitrary_types_allowed=True,
        frozen=True,
    )
    client_id: Optional[str] = None
    identity_scope: Optional[str] = None


class MetricPatterns(BaseModel):
    model_config = ConfigDict(
        arbitrary_types_allowed=True,
        frozen=True,
    )
    exclude: Optional[tuple[str, ...]] = None
    include: Optional[tuple[str, ...]] = None


class ObfuscatorOptions(BaseModel):
    model_config = ConfigDict(
        arbitrary_types_allowed=True,
        frozen=True,
    )
    collect_commands: Optional[bool] = None
    collect_comments: Optional[bool] = None
    collect_metadata: Optional[bool] = None
    collect_tables: Optional[bool] = None
    keep_dollar_quoted_func: Optional[bool] = None
    keep_sql_alias: Optional[bool] = None
    replace_digits: Optional[bool] = None


class QueryActivity(BaseModel):
    model_config = ConfigDict(
        arbitrary_types_allowed=True,
        frozen=True,
    )
    collection_interval: Optional[float] = None
    enabled: Optional[bool] = None
    payload_row_limit: Optional[float] = None


class QueryMetrics(BaseModel):
    model_config = ConfigDict(
        arbitrary_types_allowed=True,
        frozen=True,
    )
    collection_interval: Optional[float] = None
    enabled: Optional[bool] = None
    pg_stat_statements_max_warning_threshold: Optional[float] = None


class QuerySamples(BaseModel):
    model_config = ConfigDict(
        arbitrary_types_allowed=True,
        frozen=True,
    )
    collection_interval: Optional[float] = None
    enabled: Optional[bool] = None
    explain_function: Optional[str] = None
    explain_parameterized_queries: Optional[bool] = None
    explained_queries_cache_maxsize: Optional[int] = None
    explained_queries_per_hour_per_query: Optional[int] = None
    samples_per_hour_per_query: Optional[int] = None
    seen_samples_cache_maxsize: Optional[int] = None


class Relation(BaseModel):
    model_config = ConfigDict(
        arbitrary_types_allowed=True,
        frozen=True,
    )
    relation_name: Optional[str] = None
    relation_regex: Optional[str] = None
    relation_schema: Optional[str] = None
    relkind: Optional[tuple[str, ...]] = None
    schemas: Optional[tuple[str, ...]] = None


class InstanceConfig(BaseModel):
    model_config = ConfigDict(
        validate_default=True,
        arbitrary_types_allowed=True,
        frozen=True,
    )
    activity_metrics_excluded_aggregations: Optional[tuple[str, ...]] = None
    application_name: Optional[str] = None
    aws: Optional[Aws] = None
    azure: Optional[Azure] = None
    collect_activity_metrics: Optional[bool] = None
    collect_bloat_metrics: Optional[bool] = None
    collect_count_metrics: Optional[bool] = None
    collect_database_size_metrics: Optional[bool] = None
    collect_default_database: Optional[bool] = None
    collect_function_metrics: Optional[bool] = None
    collect_schemas: Optional[CollectSchemas] = None
    collect_settings: Optional[CollectSettings] = None
    collect_wal_metrics: Optional[bool] = None
    connection_timeout: Optional[int] = None
    custom_queries: Optional[tuple[MappingProxyType[str, Any], ...]] = None
    data_directory: Optional[str] = None
    database_autodiscovery: Optional[DatabaseAutodiscovery] = None
    database_instance_collection_interval: Optional[float] = None
    dbm: Optional[bool] = None
    dbname: Optional[str] = None
    dbstrict: Optional[bool] = None
    disable_generic_tags: Optional[bool] = None
    empty_default_hostname: Optional[bool] = None
    gcp: Optional[Gcp] = None
    host: str
    idle_connection_timeout: Optional[int] = None
    ignore_databases: Optional[tuple[str, ...]] = None
    log_unobfuscated_plans: Optional[bool] = None
    log_unobfuscated_queries: Optional[bool] = None
    managed_identity: Optional[ManagedIdentity] = None
    max_connections: Optional[int] = None
    max_relations: Optional[int] = None
    metric_patterns: Optional[MetricPatterns] = None
    min_collection_interval: Optional[float] = None
    obfuscator_options: Optional[ObfuscatorOptions] = None
    password: Optional[str] = None
    pg_stat_statements_view: Optional[str] = None
    port: Optional[int] = None
    query_activity: Optional[QueryActivity] = None
    query_metrics: Optional[QueryMetrics] = None
    query_samples: Optional[QuerySamples] = None
    query_timeout: Optional[int] = None
    relations: Optional[tuple[Union[str, Relation], ...]] = None
    reported_hostname: Optional[str] = None
    service: Optional[str] = None
    ssl: Optional[str] = None
    ssl_cert: Optional[str] = None
    ssl_key: Optional[str] = None
    ssl_password: Optional[str] = None
    ssl_root_cert: Optional[str] = None
    table_count_limit: Optional[int] = None
    tag_replication_role: Optional[bool] = None
    tags: Optional[tuple[str, ...]] = None
    username: str

    @model_validator(mode='before')
    def _initial_validation(cls, values):
        return validation.core.initialize_config(getattr(validators, 'initialize_instance', identity)(values))

    @field_validator('*', mode='before')
    def _validate(cls, value, info):
        field = cls.model_fields[info.field_name]
        field_name = field.alias or info.field_name
        if field_name in info.context['configured_fields']:
            value = getattr(validators, f'instance_{info.field_name}', identity)(value, field=field)
        else:
            value = getattr(defaults, f'instance_{info.field_name}', lambda: value)()

        return validation.utils.make_immutable(value)

    @model_validator(mode='after')
    def _final_validation(cls, model):
        return validation.core.check_model(getattr(validators, 'check_instance', identity)(model))
