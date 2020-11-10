from django.core.management.base import BaseCommand as BaseCommand, CommandError as CommandError
from django.db import DEFAULT_DB_ALIAS as DEFAULT_DB_ALIAS, connections as connections
from django.db.models.constants import LOOKUP_SEP as LOOKUP_SEP
from typing import Any, Dict, Iterable, List, Tuple

class Command(BaseCommand):
    stealth_options: Tuple[str] = ...
    db_module: str = ...
    def handle_inspection(self, options: Dict[str, Any]) -> Iterable[str]: ...
    def normalize_col_name(self, col_name: str, used_column_names: List[str], is_relation: bool) -> Tuple[str, Dict[str, str], List[str]]: ...
    def get_field_type(self, connection: Any, table_name: Any, row: Any) -> Tuple[str, Dict[str, str], List[str]]: ...
    def get_meta(self, table_name: str, constraints: Any, column_to_field_name: Any, is_view: Any, is_partition: Any) -> List[str]: ...
