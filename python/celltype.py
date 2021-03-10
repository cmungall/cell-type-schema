# Auto generated from celltype.yaml by pythongen.py version: 0.9.0
# Generation date: 2021-03-09 17:21
# Schema: example
#
# id: https://w3id.org/example
# description: example
# license: https://creativecommons.org/publicdomain/zero/1.0/

import dataclasses
import sys
import re
from typing import Optional, List, Union, Dict, ClassVar, Any
from dataclasses import dataclass
from biolinkml.meta import EnumDefinition, PermissibleValue, PvFormulaOptions

from biolinkml.utils.slot import Slot
from biolinkml.utils.metamodelcore import empty_list, empty_dict, bnode
from biolinkml.utils.yamlutils import YAMLRoot, extended_str, extended_float, extended_int
if sys.version_info < (3, 7, 6):
    from biolinkml.utils.dataclass_extensions_375 import dataclasses_init_fn_with_kwargs
else:
    from biolinkml.utils.dataclass_extensions_376 import dataclasses_init_fn_with_kwargs
from biolinkml.utils.formatutils import camelcase, underscore, sfx
from biolinkml.utils.enumerations import EnumDefinitionImpl
from rdflib import Namespace, URIRef
from biolinkml.utils.curienamespace import CurieNamespace
from includes.types import String

metamodel_version = "1.7.0"

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
BIOLINKML = CurieNamespace('biolinkml', 'https://w3id.org/biolink/biolinkml/')
EXAMPLE = CurieNamespace('example', 'https://w3id.org/example')
XSD = CurieNamespace('xsd', 'http://www.w3.org/2001/XMLSchema#')
DEFAULT_ = EXAMPLE


# Types
class AllenDendIdentifier(String):
    type_class_uri = XSD.string
    type_class_curie = "xsd:string"
    type_name = "AllenDend identifier"
    type_model_uri = EXAMPLE.AllenDendIdentifier


class BDSHELPIdentifier(String):
    type_class_uri = XSD.string
    type_class_curie = "xsd:string"
    type_name = "BDSHELP identifier"
    type_model_uri = EXAMPLE.BDSHELPIdentifier


class OwlIdentifier(String):
    type_class_uri = XSD.string
    type_class_curie = "xsd:string"
    type_name = "owl identifier"
    type_model_uri = EXAMPLE.OwlIdentifier


class Identifier(String):
    type_class_uri = XSD.string
    type_class_curie = "xsd:string"
    type_name = "identifier"
    type_model_uri = EXAMPLE.Identifier


class HttpIdentifier(String):
    type_class_uri = XSD.string
    type_class_curie = "xsd:string"
    type_name = "http identifier"
    type_model_uri = EXAMPLE.HttpIdentifier


class CellSetPreferredAliasIdentifier(String):
    type_class_uri = XSD.string
    type_class_curie = "xsd:string"
    type_name = "cell_set_preferred_alias identifier"
    type_model_uri = EXAMPLE.CellSetPreferredAliasIdentifier


class CLIdentifier(String):
    type_class_uri = XSD.string
    type_class_curie = "xsd:string"
    type_name = "CL identifier"
    type_model_uri = EXAMPLE.CLIdentifier


class UBERONIdentifier(String):
    type_class_uri = XSD.string
    type_class_curie = "xsd:string"
    type_name = "UBERON identifier"
    type_model_uri = EXAMPLE.UBERONIdentifier


class EnsemblIdentifier(String):
    type_class_uri = XSD.string
    type_class_curie = "xsd:string"
    type_name = "ensembl identifier"
    type_model_uri = EXAMPLE.EnsemblIdentifier


class DoiIdentifier(String):
    type_class_uri = XSD.string
    type_class_curie = "xsd:string"
    type_name = "doi identifier"
    type_model_uri = EXAMPLE.DoiIdentifier


class SOIdentifier(String):
    type_class_uri = XSD.string
    type_class_curie = "xsd:string"
    type_name = "SO identifier"
    type_model_uri = EXAMPLE.SOIdentifier


# Class references



@dataclass
class CCN201810310(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = EXAMPLE.CCN201810310
    class_class_curie: ClassVar[str] = "example:CCN201810310"
    class_name: ClassVar[str] = "CCN201810310"
    class_model_uri: ClassVar[URIRef] = EXAMPLE.CCN201810310

    ID: Optional[Union[str, AllenDendIdentifier]] = None
    Label: Optional[str] = None
    PrefLabel: Optional[str] = None
    Entity_Type: Optional[Union[str, BDSHELPIdentifier]] = None
    TYPE: Optional[Union[str, "TYPEEnum"]] = None
    Property_Assertions: Optional[Union[str, AllenDendIdentifier]] = None
    Synonyms: Optional[Union[str, List[str]]] = empty_list()
    Function: Optional[Union[str, "FunctionEnum"]] = None
    cell_set_preferred_alias: Optional[str] = None
    original_label: Optional[str] = None
    cell_set_label: Optional[str] = None
    cell_set_aligned_alias: Optional[str] = None
    cell_set_additional_aliases: Optional[Union[str, "CellSetAdditionalAliasesEnum"]] = None
    cell_set_alias_assignee: Optional[Union[str, "CellSetAliasAssigneeEnum"]] = None
    cell_set_alias_citation: Optional[Union[str, "CellSetAliasCitationEnum"]] = None
    Metadata: Optional[Union[str, Identifier]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.ID is not None and not isinstance(self.ID, AllenDendIdentifier):
            self.ID = AllenDendIdentifier(self.ID)

        if self.Label is not None and not isinstance(self.Label, str):
            self.Label = str(self.Label)

        if self.PrefLabel is not None and not isinstance(self.PrefLabel, str):
            self.PrefLabel = str(self.PrefLabel)

        if self.Entity_Type is not None and not isinstance(self.Entity_Type, BDSHELPIdentifier):
            self.Entity_Type = BDSHELPIdentifier(self.Entity_Type)

        if self.TYPE is not None and not isinstance(self.TYPE, TYPEEnum):
            self.TYPE = TYPEEnum(self.TYPE)

        if self.Property_Assertions is not None and not isinstance(self.Property_Assertions, AllenDendIdentifier):
            self.Property_Assertions = AllenDendIdentifier(self.Property_Assertions)

        if self.Synonyms is None:
            self.Synonyms = []
        if not isinstance(self.Synonyms, list):
            self.Synonyms = [self.Synonyms]
        self.Synonyms = [v if isinstance(v, str) else str(v) for v in self.Synonyms]

        if self.Function is not None and not isinstance(self.Function, FunctionEnum):
            self.Function = FunctionEnum(self.Function)

        if self.cell_set_preferred_alias is not None and not isinstance(self.cell_set_preferred_alias, str):
            self.cell_set_preferred_alias = str(self.cell_set_preferred_alias)

        if self.original_label is not None and not isinstance(self.original_label, str):
            self.original_label = str(self.original_label)

        if self.cell_set_label is not None and not isinstance(self.cell_set_label, str):
            self.cell_set_label = str(self.cell_set_label)

        if self.cell_set_aligned_alias is not None and not isinstance(self.cell_set_aligned_alias, str):
            self.cell_set_aligned_alias = str(self.cell_set_aligned_alias)

        if self.cell_set_additional_aliases is not None and not isinstance(self.cell_set_additional_aliases, CellSetAdditionalAliasesEnum):
            self.cell_set_additional_aliases = CellSetAdditionalAliasesEnum(self.cell_set_additional_aliases)

        if self.cell_set_alias_assignee is not None and not isinstance(self.cell_set_alias_assignee, CellSetAliasAssigneeEnum):
            self.cell_set_alias_assignee = CellSetAliasAssigneeEnum(self.cell_set_alias_assignee)

        if self.cell_set_alias_citation is not None and not isinstance(self.cell_set_alias_citation, CellSetAliasCitationEnum):
            self.cell_set_alias_citation = CellSetAliasCitationEnum(self.cell_set_alias_citation)

        if self.Metadata is not None and not isinstance(self.Metadata, Identifier):
            self.Metadata = Identifier(self.Metadata)

        super().__post_init__(**kwargs)


@dataclass
class CCN201810310Class(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = EXAMPLE.CCN201810310Class
    class_class_curie: ClassVar[str] = "example:CCN201810310Class"
    class_name: ClassVar[str] = "CCN201810310_class"
    class_model_uri: ClassVar[URIRef] = EXAMPLE.CCN201810310Class

    ID: Optional[Union[str, AllenDendIdentifier]] = None
    Label: Optional[str] = None
    Synonyms_from_taxonomy: Optional[Union[str, List[str]]] = empty_list()
    Curated_synonyms: Optional[Union[str, "CuratedSynonymsEnum"]] = None
    Comment: Optional[Union[str, CellSetPreferredAliasIdentifier]] = None
    Classification: Optional[Union[str, "ClassificationEnum"]] = None
    Classification_comment: Optional[Union[str, "ClassificationCommentEnum"]] = None
    Classification_pub: Optional[Union[str, "ClassificationPubEnum"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.ID is not None and not isinstance(self.ID, AllenDendIdentifier):
            self.ID = AllenDendIdentifier(self.ID)

        if self.Label is not None and not isinstance(self.Label, str):
            self.Label = str(self.Label)

        if self.Synonyms_from_taxonomy is None:
            self.Synonyms_from_taxonomy = []
        if not isinstance(self.Synonyms_from_taxonomy, list):
            self.Synonyms_from_taxonomy = [self.Synonyms_from_taxonomy]
        self.Synonyms_from_taxonomy = [v if isinstance(v, str) else str(v) for v in self.Synonyms_from_taxonomy]

        if self.Curated_synonyms is not None and not isinstance(self.Curated_synonyms, CuratedSynonymsEnum):
            self.Curated_synonyms = CuratedSynonymsEnum(self.Curated_synonyms)

        if self.Comment is not None and not isinstance(self.Comment, CellSetPreferredAliasIdentifier):
            self.Comment = CellSetPreferredAliasIdentifier(self.Comment)

        if self.Classification is not None and not isinstance(self.Classification, ClassificationEnum):
            self.Classification = ClassificationEnum(self.Classification)

        if self.Classification_comment is not None and not isinstance(self.Classification_comment, ClassificationCommentEnum):
            self.Classification_comment = ClassificationCommentEnum(self.Classification_comment)

        if self.Classification_pub is not None and not isinstance(self.Classification_pub, ClassificationPubEnum):
            self.Classification_pub = ClassificationPubEnum(self.Classification_pub)

        super().__post_init__(**kwargs)


@dataclass
class CCN201810310EquivalentReification(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = EXAMPLE.CCN201810310EquivalentReification
    class_class_curie: ClassVar[str] = "example:CCN201810310EquivalentReification"
    class_name: ClassVar[str] = "CCN201810310_equivalent_reification"
    class_model_uri: ClassVar[URIRef] = EXAMPLE.CCN201810310EquivalentReification

    ID: Optional[Union[str, AllenDendIdentifier]] = None
    Exemplar: Optional[Union[str, AllenDendIdentifier]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.ID is not None and not isinstance(self.ID, AllenDendIdentifier):
            self.ID = AllenDendIdentifier(self.ID)

        if self.Exemplar is not None and not isinstance(self.Exemplar, AllenDendIdentifier):
            self.Exemplar = AllenDendIdentifier(self.Exemplar)

        super().__post_init__(**kwargs)


class CCN201810310Markers(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = EXAMPLE.CCN201810310Markers
    class_class_curie: ClassVar[str] = "example:CCN201810310Markers"
    class_name: ClassVar[str] = "CCN201810310_markers"
    class_model_uri: ClassVar[URIRef] = EXAMPLE.CCN201810310Markers


@dataclass
class CCN201908210(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = EXAMPLE.CCN201908210
    class_class_curie: ClassVar[str] = "example:CCN201908210"
    class_name: ClassVar[str] = "CCN201908210"
    class_model_uri: ClassVar[URIRef] = EXAMPLE.CCN201908210

    ID: Optional[Union[str, AllenDendIdentifier]] = None
    Label: Optional[str] = None
    PrefLabel: Optional[str] = None
    Entity_Type: Optional[Union[str, BDSHELPIdentifier]] = None
    TYPE: Optional[Union[str, "TYPEEnum"]] = None
    Property_Assertions: Optional[Union[str, AllenDendIdentifier]] = None
    Synonyms: Optional[Union[str, List[str]]] = empty_list()
    Function: Optional[Union[str, "FunctionEnum"]] = None
    cell_set_preferred_alias: Optional[str] = None
    original_label: Optional[str] = None
    cell_set_label: Optional[str] = None
    cell_set_aligned_alias: Optional[str] = None
    cell_set_additional_aliases: Optional[Union[str, "CellSetAdditionalAliasesEnum"]] = None
    cell_set_alias_assignee: Optional[Union[str, "CellSetAliasAssigneeEnum"]] = None
    cell_set_alias_citation: Optional[Union[str, "CellSetAliasCitationEnum"]] = None
    Metadata: Optional[Union[str, Identifier]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.ID is not None and not isinstance(self.ID, AllenDendIdentifier):
            self.ID = AllenDendIdentifier(self.ID)

        if self.Label is not None and not isinstance(self.Label, str):
            self.Label = str(self.Label)

        if self.PrefLabel is not None and not isinstance(self.PrefLabel, str):
            self.PrefLabel = str(self.PrefLabel)

        if self.Entity_Type is not None and not isinstance(self.Entity_Type, BDSHELPIdentifier):
            self.Entity_Type = BDSHELPIdentifier(self.Entity_Type)

        if self.TYPE is not None and not isinstance(self.TYPE, TYPEEnum):
            self.TYPE = TYPEEnum(self.TYPE)

        if self.Property_Assertions is not None and not isinstance(self.Property_Assertions, AllenDendIdentifier):
            self.Property_Assertions = AllenDendIdentifier(self.Property_Assertions)

        if self.Synonyms is None:
            self.Synonyms = []
        if not isinstance(self.Synonyms, list):
            self.Synonyms = [self.Synonyms]
        self.Synonyms = [v if isinstance(v, str) else str(v) for v in self.Synonyms]

        if self.Function is not None and not isinstance(self.Function, FunctionEnum):
            self.Function = FunctionEnum(self.Function)

        if self.cell_set_preferred_alias is not None and not isinstance(self.cell_set_preferred_alias, str):
            self.cell_set_preferred_alias = str(self.cell_set_preferred_alias)

        if self.original_label is not None and not isinstance(self.original_label, str):
            self.original_label = str(self.original_label)

        if self.cell_set_label is not None and not isinstance(self.cell_set_label, str):
            self.cell_set_label = str(self.cell_set_label)

        if self.cell_set_aligned_alias is not None and not isinstance(self.cell_set_aligned_alias, str):
            self.cell_set_aligned_alias = str(self.cell_set_aligned_alias)

        if self.cell_set_additional_aliases is not None and not isinstance(self.cell_set_additional_aliases, CellSetAdditionalAliasesEnum):
            self.cell_set_additional_aliases = CellSetAdditionalAliasesEnum(self.cell_set_additional_aliases)

        if self.cell_set_alias_assignee is not None and not isinstance(self.cell_set_alias_assignee, CellSetAliasAssigneeEnum):
            self.cell_set_alias_assignee = CellSetAliasAssigneeEnum(self.cell_set_alias_assignee)

        if self.cell_set_alias_citation is not None and not isinstance(self.cell_set_alias_citation, CellSetAliasCitationEnum):
            self.cell_set_alias_citation = CellSetAliasCitationEnum(self.cell_set_alias_citation)

        if self.Metadata is not None and not isinstance(self.Metadata, Identifier):
            self.Metadata = Identifier(self.Metadata)

        super().__post_init__(**kwargs)


@dataclass
class CCN201908210Class(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = EXAMPLE.CCN201908210Class
    class_class_curie: ClassVar[str] = "example:CCN201908210Class"
    class_name: ClassVar[str] = "CCN201908210_class"
    class_model_uri: ClassVar[URIRef] = EXAMPLE.CCN201908210Class

    ID: Optional[Union[str, AllenDendIdentifier]] = None
    Label: Optional[str] = None
    Synonyms_from_taxonomy: Optional[Union[str, List[str]]] = empty_list()
    Curated_synonyms: Optional[Union[str, "CuratedSynonymsEnum"]] = None
    Comment: Optional[Union[str, CellSetPreferredAliasIdentifier]] = None
    Classification: Optional[Union[str, "ClassificationEnum"]] = None
    Classification_comment: Optional[Union[str, "ClassificationCommentEnum"]] = None
    Classification_pub: Optional[Union[str, "ClassificationPubEnum"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.ID is not None and not isinstance(self.ID, AllenDendIdentifier):
            self.ID = AllenDendIdentifier(self.ID)

        if self.Label is not None and not isinstance(self.Label, str):
            self.Label = str(self.Label)

        if self.Synonyms_from_taxonomy is None:
            self.Synonyms_from_taxonomy = []
        if not isinstance(self.Synonyms_from_taxonomy, list):
            self.Synonyms_from_taxonomy = [self.Synonyms_from_taxonomy]
        self.Synonyms_from_taxonomy = [v if isinstance(v, str) else str(v) for v in self.Synonyms_from_taxonomy]

        if self.Curated_synonyms is not None and not isinstance(self.Curated_synonyms, CuratedSynonymsEnum):
            self.Curated_synonyms = CuratedSynonymsEnum(self.Curated_synonyms)

        if self.Comment is not None and not isinstance(self.Comment, CellSetPreferredAliasIdentifier):
            self.Comment = CellSetPreferredAliasIdentifier(self.Comment)

        if self.Classification is not None and not isinstance(self.Classification, ClassificationEnum):
            self.Classification = ClassificationEnum(self.Classification)

        if self.Classification_comment is not None and not isinstance(self.Classification_comment, ClassificationCommentEnum):
            self.Classification_comment = ClassificationCommentEnum(self.Classification_comment)

        if self.Classification_pub is not None and not isinstance(self.Classification_pub, ClassificationPubEnum):
            self.Classification_pub = ClassificationPubEnum(self.Classification_pub)

        super().__post_init__(**kwargs)


@dataclass
class CCN201908210EquivalentReification(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = EXAMPLE.CCN201908210EquivalentReification
    class_class_curie: ClassVar[str] = "example:CCN201908210EquivalentReification"
    class_name: ClassVar[str] = "CCN201908210_equivalent_reification"
    class_model_uri: ClassVar[URIRef] = EXAMPLE.CCN201908210EquivalentReification

    ID: Optional[Union[str, AllenDendIdentifier]] = None
    Exemplar: Optional[Union[str, AllenDendIdentifier]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.ID is not None and not isinstance(self.ID, AllenDendIdentifier):
            self.ID = AllenDendIdentifier(self.ID)

        if self.Exemplar is not None and not isinstance(self.Exemplar, AllenDendIdentifier):
            self.Exemplar = AllenDendIdentifier(self.Exemplar)

        super().__post_init__(**kwargs)


class CCN201908210Markers(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = EXAMPLE.CCN201908210Markers
    class_class_curie: ClassVar[str] = "example:CCN201908210Markers"
    class_name: ClassVar[str] = "CCN201908210_markers"
    class_model_uri: ClassVar[URIRef] = EXAMPLE.CCN201908210Markers


@dataclass
class CCN201908211(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = EXAMPLE.CCN201908211
    class_class_curie: ClassVar[str] = "example:CCN201908211"
    class_name: ClassVar[str] = "CCN201908211"
    class_model_uri: ClassVar[URIRef] = EXAMPLE.CCN201908211

    ID: Optional[Union[str, AllenDendIdentifier]] = None
    Label: Optional[str] = None
    PrefLabel: Optional[str] = None
    Entity_Type: Optional[Union[str, BDSHELPIdentifier]] = None
    TYPE: Optional[Union[str, "TYPEEnum"]] = None
    Property_Assertions: Optional[Union[str, AllenDendIdentifier]] = None
    Synonyms: Optional[Union[str, List[str]]] = empty_list()
    Function: Optional[Union[str, "FunctionEnum"]] = None
    cell_set_preferred_alias: Optional[str] = None
    original_label: Optional[str] = None
    cell_set_label: Optional[str] = None
    cell_set_aligned_alias: Optional[str] = None
    cell_set_additional_aliases: Optional[Union[str, "CellSetAdditionalAliasesEnum"]] = None
    cell_set_alias_assignee: Optional[Union[str, "CellSetAliasAssigneeEnum"]] = None
    cell_set_alias_citation: Optional[Union[str, "CellSetAliasCitationEnum"]] = None
    Metadata: Optional[Union[str, Identifier]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.ID is not None and not isinstance(self.ID, AllenDendIdentifier):
            self.ID = AllenDendIdentifier(self.ID)

        if self.Label is not None and not isinstance(self.Label, str):
            self.Label = str(self.Label)

        if self.PrefLabel is not None and not isinstance(self.PrefLabel, str):
            self.PrefLabel = str(self.PrefLabel)

        if self.Entity_Type is not None and not isinstance(self.Entity_Type, BDSHELPIdentifier):
            self.Entity_Type = BDSHELPIdentifier(self.Entity_Type)

        if self.TYPE is not None and not isinstance(self.TYPE, TYPEEnum):
            self.TYPE = TYPEEnum(self.TYPE)

        if self.Property_Assertions is not None and not isinstance(self.Property_Assertions, AllenDendIdentifier):
            self.Property_Assertions = AllenDendIdentifier(self.Property_Assertions)

        if self.Synonyms is None:
            self.Synonyms = []
        if not isinstance(self.Synonyms, list):
            self.Synonyms = [self.Synonyms]
        self.Synonyms = [v if isinstance(v, str) else str(v) for v in self.Synonyms]

        if self.Function is not None and not isinstance(self.Function, FunctionEnum):
            self.Function = FunctionEnum(self.Function)

        if self.cell_set_preferred_alias is not None and not isinstance(self.cell_set_preferred_alias, str):
            self.cell_set_preferred_alias = str(self.cell_set_preferred_alias)

        if self.original_label is not None and not isinstance(self.original_label, str):
            self.original_label = str(self.original_label)

        if self.cell_set_label is not None and not isinstance(self.cell_set_label, str):
            self.cell_set_label = str(self.cell_set_label)

        if self.cell_set_aligned_alias is not None and not isinstance(self.cell_set_aligned_alias, str):
            self.cell_set_aligned_alias = str(self.cell_set_aligned_alias)

        if self.cell_set_additional_aliases is not None and not isinstance(self.cell_set_additional_aliases, CellSetAdditionalAliasesEnum):
            self.cell_set_additional_aliases = CellSetAdditionalAliasesEnum(self.cell_set_additional_aliases)

        if self.cell_set_alias_assignee is not None and not isinstance(self.cell_set_alias_assignee, CellSetAliasAssigneeEnum):
            self.cell_set_alias_assignee = CellSetAliasAssigneeEnum(self.cell_set_alias_assignee)

        if self.cell_set_alias_citation is not None and not isinstance(self.cell_set_alias_citation, CellSetAliasCitationEnum):
            self.cell_set_alias_citation = CellSetAliasCitationEnum(self.cell_set_alias_citation)

        if self.Metadata is not None and not isinstance(self.Metadata, Identifier):
            self.Metadata = Identifier(self.Metadata)

        super().__post_init__(**kwargs)


@dataclass
class CCN201908211Class(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = EXAMPLE.CCN201908211Class
    class_class_curie: ClassVar[str] = "example:CCN201908211Class"
    class_name: ClassVar[str] = "CCN201908211_class"
    class_model_uri: ClassVar[URIRef] = EXAMPLE.CCN201908211Class

    ID: Optional[Union[str, AllenDendIdentifier]] = None
    Label: Optional[str] = None
    Synonyms_from_taxonomy: Optional[Union[str, List[str]]] = empty_list()
    Curated_synonyms: Optional[Union[str, "CuratedSynonymsEnum"]] = None
    Comment: Optional[Union[str, CellSetPreferredAliasIdentifier]] = None
    Classification: Optional[Union[str, "ClassificationEnum"]] = None
    Classification_comment: Optional[Union[str, "ClassificationCommentEnum"]] = None
    Classification_pub: Optional[Union[str, "ClassificationPubEnum"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.ID is not None and not isinstance(self.ID, AllenDendIdentifier):
            self.ID = AllenDendIdentifier(self.ID)

        if self.Label is not None and not isinstance(self.Label, str):
            self.Label = str(self.Label)

        if self.Synonyms_from_taxonomy is None:
            self.Synonyms_from_taxonomy = []
        if not isinstance(self.Synonyms_from_taxonomy, list):
            self.Synonyms_from_taxonomy = [self.Synonyms_from_taxonomy]
        self.Synonyms_from_taxonomy = [v if isinstance(v, str) else str(v) for v in self.Synonyms_from_taxonomy]

        if self.Curated_synonyms is not None and not isinstance(self.Curated_synonyms, CuratedSynonymsEnum):
            self.Curated_synonyms = CuratedSynonymsEnum(self.Curated_synonyms)

        if self.Comment is not None and not isinstance(self.Comment, CellSetPreferredAliasIdentifier):
            self.Comment = CellSetPreferredAliasIdentifier(self.Comment)

        if self.Classification is not None and not isinstance(self.Classification, ClassificationEnum):
            self.Classification = ClassificationEnum(self.Classification)

        if self.Classification_comment is not None and not isinstance(self.Classification_comment, ClassificationCommentEnum):
            self.Classification_comment = ClassificationCommentEnum(self.Classification_comment)

        if self.Classification_pub is not None and not isinstance(self.Classification_pub, ClassificationPubEnum):
            self.Classification_pub = ClassificationPubEnum(self.Classification_pub)

        super().__post_init__(**kwargs)


@dataclass
class CCN201908211EquivalentReification(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = EXAMPLE.CCN201908211EquivalentReification
    class_class_curie: ClassVar[str] = "example:CCN201908211EquivalentReification"
    class_name: ClassVar[str] = "CCN201908211_equivalent_reification"
    class_model_uri: ClassVar[URIRef] = EXAMPLE.CCN201908211EquivalentReification

    ID: Optional[Union[str, AllenDendIdentifier]] = None
    Exemplar: Optional[Union[str, AllenDendIdentifier]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.ID is not None and not isinstance(self.ID, AllenDendIdentifier):
            self.ID = AllenDendIdentifier(self.ID)

        if self.Exemplar is not None and not isinstance(self.Exemplar, AllenDendIdentifier):
            self.Exemplar = AllenDendIdentifier(self.Exemplar)

        super().__post_init__(**kwargs)


class CCN201908211Markers(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = EXAMPLE.CCN201908211Markers
    class_class_curie: ClassVar[str] = "example:CCN201908211Markers"
    class_name: ClassVar[str] = "CCN201908211_markers"
    class_model_uri: ClassVar[URIRef] = EXAMPLE.CCN201908211Markers


@dataclass
class CCN202002013(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = EXAMPLE.CCN202002013
    class_class_curie: ClassVar[str] = "example:CCN202002013"
    class_name: ClassVar[str] = "CCN202002013"
    class_model_uri: ClassVar[URIRef] = EXAMPLE.CCN202002013

    ID: Optional[Union[str, AllenDendIdentifier]] = None
    Label: Optional[str] = None
    PrefLabel: Optional[str] = None
    Entity_Type: Optional[Union[str, BDSHELPIdentifier]] = None
    TYPE: Optional[Union[str, "TYPEEnum"]] = None
    Property_Assertions: Optional[Union[str, AllenDendIdentifier]] = None
    Synonyms: Optional[Union[str, List[str]]] = empty_list()
    Function: Optional[Union[str, "FunctionEnum"]] = None
    cell_set_preferred_alias: Optional[str] = None
    original_label: Optional[str] = None
    cell_set_label: Optional[str] = None
    cell_set_aligned_alias: Optional[str] = None
    cell_set_additional_aliases: Optional[Union[str, "CellSetAdditionalAliasesEnum"]] = None
    cell_set_alias_assignee: Optional[Union[str, "CellSetAliasAssigneeEnum"]] = None
    cell_set_alias_citation: Optional[Union[str, "CellSetAliasCitationEnum"]] = None
    Metadata: Optional[Union[str, Identifier]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.ID is not None and not isinstance(self.ID, AllenDendIdentifier):
            self.ID = AllenDendIdentifier(self.ID)

        if self.Label is not None and not isinstance(self.Label, str):
            self.Label = str(self.Label)

        if self.PrefLabel is not None and not isinstance(self.PrefLabel, str):
            self.PrefLabel = str(self.PrefLabel)

        if self.Entity_Type is not None and not isinstance(self.Entity_Type, BDSHELPIdentifier):
            self.Entity_Type = BDSHELPIdentifier(self.Entity_Type)

        if self.TYPE is not None and not isinstance(self.TYPE, TYPEEnum):
            self.TYPE = TYPEEnum(self.TYPE)

        if self.Property_Assertions is not None and not isinstance(self.Property_Assertions, AllenDendIdentifier):
            self.Property_Assertions = AllenDendIdentifier(self.Property_Assertions)

        if self.Synonyms is None:
            self.Synonyms = []
        if not isinstance(self.Synonyms, list):
            self.Synonyms = [self.Synonyms]
        self.Synonyms = [v if isinstance(v, str) else str(v) for v in self.Synonyms]

        if self.Function is not None and not isinstance(self.Function, FunctionEnum):
            self.Function = FunctionEnum(self.Function)

        if self.cell_set_preferred_alias is not None and not isinstance(self.cell_set_preferred_alias, str):
            self.cell_set_preferred_alias = str(self.cell_set_preferred_alias)

        if self.original_label is not None and not isinstance(self.original_label, str):
            self.original_label = str(self.original_label)

        if self.cell_set_label is not None and not isinstance(self.cell_set_label, str):
            self.cell_set_label = str(self.cell_set_label)

        if self.cell_set_aligned_alias is not None and not isinstance(self.cell_set_aligned_alias, str):
            self.cell_set_aligned_alias = str(self.cell_set_aligned_alias)

        if self.cell_set_additional_aliases is not None and not isinstance(self.cell_set_additional_aliases, CellSetAdditionalAliasesEnum):
            self.cell_set_additional_aliases = CellSetAdditionalAliasesEnum(self.cell_set_additional_aliases)

        if self.cell_set_alias_assignee is not None and not isinstance(self.cell_set_alias_assignee, CellSetAliasAssigneeEnum):
            self.cell_set_alias_assignee = CellSetAliasAssigneeEnum(self.cell_set_alias_assignee)

        if self.cell_set_alias_citation is not None and not isinstance(self.cell_set_alias_citation, CellSetAliasCitationEnum):
            self.cell_set_alias_citation = CellSetAliasCitationEnum(self.cell_set_alias_citation)

        if self.Metadata is not None and not isinstance(self.Metadata, Identifier):
            self.Metadata = Identifier(self.Metadata)

        super().__post_init__(**kwargs)


@dataclass
class CCN202002013Class(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = EXAMPLE.CCN202002013Class
    class_class_curie: ClassVar[str] = "example:CCN202002013Class"
    class_name: ClassVar[str] = "CCN202002013_class"
    class_model_uri: ClassVar[URIRef] = EXAMPLE.CCN202002013Class

    ID: Optional[Union[str, AllenDendIdentifier]] = None
    Label: Optional[str] = None
    Synonyms_from_taxonomy: Optional[Union[str, List[str]]] = empty_list()
    Curated_synonyms: Optional[Union[str, "CuratedSynonymsEnum"]] = None
    Comment: Optional[Union[str, CellSetPreferredAliasIdentifier]] = None
    Classification: Optional[Union[str, "ClassificationEnum"]] = None
    Classification_comment: Optional[Union[str, "ClassificationCommentEnum"]] = None
    Classification_pub: Optional[Union[str, "ClassificationPubEnum"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.ID is not None and not isinstance(self.ID, AllenDendIdentifier):
            self.ID = AllenDendIdentifier(self.ID)

        if self.Label is not None and not isinstance(self.Label, str):
            self.Label = str(self.Label)

        if self.Synonyms_from_taxonomy is None:
            self.Synonyms_from_taxonomy = []
        if not isinstance(self.Synonyms_from_taxonomy, list):
            self.Synonyms_from_taxonomy = [self.Synonyms_from_taxonomy]
        self.Synonyms_from_taxonomy = [v if isinstance(v, str) else str(v) for v in self.Synonyms_from_taxonomy]

        if self.Curated_synonyms is not None and not isinstance(self.Curated_synonyms, CuratedSynonymsEnum):
            self.Curated_synonyms = CuratedSynonymsEnum(self.Curated_synonyms)

        if self.Comment is not None and not isinstance(self.Comment, CellSetPreferredAliasIdentifier):
            self.Comment = CellSetPreferredAliasIdentifier(self.Comment)

        if self.Classification is not None and not isinstance(self.Classification, ClassificationEnum):
            self.Classification = ClassificationEnum(self.Classification)

        if self.Classification_comment is not None and not isinstance(self.Classification_comment, ClassificationCommentEnum):
            self.Classification_comment = ClassificationCommentEnum(self.Classification_comment)

        if self.Classification_pub is not None and not isinstance(self.Classification_pub, ClassificationPubEnum):
            self.Classification_pub = ClassificationPubEnum(self.Classification_pub)

        super().__post_init__(**kwargs)


@dataclass
class CCN202002013EquivalentMarkers(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = EXAMPLE.CCN202002013EquivalentMarkers
    class_class_curie: ClassVar[str] = "example:CCN202002013EquivalentMarkers"
    class_name: ClassVar[str] = "CCN202002013_equivalent_markers"
    class_model_uri: ClassVar[URIRef] = EXAMPLE.CCN202002013EquivalentMarkers

    ID: Optional[Union[str, AllenDendIdentifier]] = None
    CLASS_TYPE: Optional[Union[str, "CLASSTYPEEnum"]] = None
    Evidence: Optional[Union[str, HttpIdentifier]] = None
    Gross_cell_type: Optional[Union[str, CLIdentifier]] = None
    Brain_region: Optional[Union[str, UBERONIdentifier]] = None
    Marker1: Optional[Union[str, EnsemblIdentifier]] = None
    Marker2: Optional[Union[str, EnsemblIdentifier]] = None
    Marker3: Optional[Union[str, EnsemblIdentifier]] = None
    Marker4: Optional[Union[str, EnsemblIdentifier]] = None
    Marker5: Optional[Union[str, EnsemblIdentifier]] = None
    Marker6: Optional[Union[str, EnsemblIdentifier]] = None
    Marker7: Optional[Union[str, EnsemblIdentifier]] = None
    Marker8: Optional[Union[str, EnsemblIdentifier]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.ID is not None and not isinstance(self.ID, AllenDendIdentifier):
            self.ID = AllenDendIdentifier(self.ID)

        if self.CLASS_TYPE is not None and not isinstance(self.CLASS_TYPE, CLASSTYPEEnum):
            self.CLASS_TYPE = CLASSTYPEEnum(self.CLASS_TYPE)

        if self.Evidence is not None and not isinstance(self.Evidence, HttpIdentifier):
            self.Evidence = HttpIdentifier(self.Evidence)

        if self.Gross_cell_type is not None and not isinstance(self.Gross_cell_type, CLIdentifier):
            self.Gross_cell_type = CLIdentifier(self.Gross_cell_type)

        if self.Brain_region is not None and not isinstance(self.Brain_region, UBERONIdentifier):
            self.Brain_region = UBERONIdentifier(self.Brain_region)

        if self.Marker1 is not None and not isinstance(self.Marker1, EnsemblIdentifier):
            self.Marker1 = EnsemblIdentifier(self.Marker1)

        if self.Marker2 is not None and not isinstance(self.Marker2, EnsemblIdentifier):
            self.Marker2 = EnsemblIdentifier(self.Marker2)

        if self.Marker3 is not None and not isinstance(self.Marker3, EnsemblIdentifier):
            self.Marker3 = EnsemblIdentifier(self.Marker3)

        if self.Marker4 is not None and not isinstance(self.Marker4, EnsemblIdentifier):
            self.Marker4 = EnsemblIdentifier(self.Marker4)

        if self.Marker5 is not None and not isinstance(self.Marker5, EnsemblIdentifier):
            self.Marker5 = EnsemblIdentifier(self.Marker5)

        if self.Marker6 is not None and not isinstance(self.Marker6, EnsemblIdentifier):
            self.Marker6 = EnsemblIdentifier(self.Marker6)

        if self.Marker7 is not None and not isinstance(self.Marker7, EnsemblIdentifier):
            self.Marker7 = EnsemblIdentifier(self.Marker7)

        if self.Marker8 is not None and not isinstance(self.Marker8, EnsemblIdentifier):
            self.Marker8 = EnsemblIdentifier(self.Marker8)

        super().__post_init__(**kwargs)


@dataclass
class CCN202002013EquivalentReification(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = EXAMPLE.CCN202002013EquivalentReification
    class_class_curie: ClassVar[str] = "example:CCN202002013EquivalentReification"
    class_name: ClassVar[str] = "CCN202002013_equivalent_reification"
    class_model_uri: ClassVar[URIRef] = EXAMPLE.CCN202002013EquivalentReification

    ID: Optional[Union[str, AllenDendIdentifier]] = None
    Exemplar: Optional[Union[str, AllenDendIdentifier]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.ID is not None and not isinstance(self.ID, AllenDendIdentifier):
            self.ID = AllenDendIdentifier(self.ID)

        if self.Exemplar is not None and not isinstance(self.Exemplar, AllenDendIdentifier):
            self.Exemplar = AllenDendIdentifier(self.Exemplar)

        super().__post_init__(**kwargs)


@dataclass
class CCN202002013Markers(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = EXAMPLE.CCN202002013Markers
    class_class_curie: ClassVar[str] = "example:CCN202002013Markers"
    class_name: ClassVar[str] = "CCN202002013_markers"
    class_model_uri: ClassVar[URIRef] = EXAMPLE.CCN202002013Markers

    ID: Optional[Union[str, AllenDendIdentifier]] = None
    TYPE: Optional[Union[str, "TYPEEnum"]] = None
    Expresses: Optional[Union[Union[str, EnsemblIdentifier], List[Union[str, EnsemblIdentifier]]]] = empty_list()
    Evidence_-_pub: Optional[Union[str, DoiIdentifier]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.ID is not None and not isinstance(self.ID, AllenDendIdentifier):
            self.ID = AllenDendIdentifier(self.ID)

        if self.TYPE is not None and not isinstance(self.TYPE, TYPEEnum):
            self.TYPE = TYPEEnum(self.TYPE)

        if self.Expresses is None:
            self.Expresses = []
        if not isinstance(self.Expresses, list):
            self.Expresses = [self.Expresses]
        self.Expresses = [v if isinstance(v, EnsemblIdentifier) else EnsemblIdentifier(v) for v in self.Expresses]

        if self.Evidence_-_pub is not None and not isinstance(self.Evidence_-_pub, DoiIdentifier):
            self.Evidence_-_pub = DoiIdentifier(self.Evidence_-_pub)

        super().__post_init__(**kwargs)


@dataclass
class CS202002013MarkersDenormalized(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = EXAMPLE.CS202002013MarkersDenormalized
    class_class_curie: ClassVar[str] = "example:CS202002013MarkersDenormalized"
    class_name: ClassVar[str] = "CS202002013_markers_denormalized"
    class_model_uri: ClassVar[URIRef] = EXAMPLE.CS202002013MarkersDenormalized

    Taxonomy_node_ID: Optional[str] = None
    clusterName: Optional[str] = None
    Markers_Delimited: Optional[Union[Union[str, EnsemblIdentifier], List[Union[str, EnsemblIdentifier]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.Taxonomy_node_ID is not None and not isinstance(self.Taxonomy_node_ID, str):
            self.Taxonomy_node_ID = str(self.Taxonomy_node_ID)

        if self.clusterName is not None and not isinstance(self.clusterName, str):
            self.clusterName = str(self.clusterName)

        if self.Markers_Delimited is None:
            self.Markers_Delimited = []
        if not isinstance(self.Markers_Delimited, list):
            self.Markers_Delimited = [self.Markers_Delimited]
        self.Markers_Delimited = [v if isinstance(v, EnsemblIdentifier) else EnsemblIdentifier(v) for v in self.Markers_Delimited]

        super().__post_init__(**kwargs)


@dataclass
class Ensmusg(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = EXAMPLE.Ensmusg
    class_class_curie: ClassVar[str] = "example:Ensmusg"
    class_name: ClassVar[str] = "ensmusg"
    class_model_uri: ClassVar[URIRef] = EXAMPLE.Ensmusg

    ID: Optional[Union[str, AllenDendIdentifier]] = None
    TYPE: Optional[Union[str, "TYPEEnum"]] = None
    NAME: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.ID is not None and not isinstance(self.ID, AllenDendIdentifier):
            self.ID = AllenDendIdentifier(self.ID)

        if self.TYPE is not None and not isinstance(self.TYPE, TYPEEnum):
            self.TYPE = TYPEEnum(self.TYPE)

        if self.NAME is not None and not isinstance(self.NAME, str):
            self.NAME = str(self.NAME)

        super().__post_init__(**kwargs)


# Enumerations
class TYPEEnum(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="TYPEEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "owl:NamedIndividual",
                PermissibleValue(text="owl:NamedIndividual",
                                 description="owl:NamedIndividual") )

class FunctionEnum(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="FunctionEnum",
    )

class CellSetAdditionalAliasesEnum(EnumDefinitionImpl):

    Neuronal = PermissibleValue(text="Neuronal",
                                       description="Neuronal")
    L6 = PermissibleValue(text="L6",
                           description="L6")
    Serpinf1 = PermissibleValue(text="Serpinf1",
                                       description="Serpinf1")

    _defn = EnumDefinition(
        name="CellSetAdditionalAliasesEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Lamp5 Rosehip",
                PermissibleValue(text="Lamp5 Rosehip",
                                 description="Lamp5 Rosehip") )
        setattr(cls, "L5 IT (ALM)",
                PermissibleValue(text="L5 IT (ALM)",
                                 description="L5 IT (ALM)") )
        setattr(cls, "L5 PT",
                PermissibleValue(text="L5 PT",
                                 description="L5 PT") )
        setattr(cls, "Cajal Retzius",
                PermissibleValue(text="Cajal Retzius",
                                 description="Cajal Retzius") )
        setattr(cls, "L5 IT (VISp)",
                PermissibleValue(text="L5 IT (VISp)",
                                 description="L5 IT (VISp)") )
        setattr(cls, "L6 IT (ALM)",
                PermissibleValue(text="L6 IT (ALM)",
                                 description="L6 IT (ALM)") )
        setattr(cls, "L6 IT (VISp)",
                PermissibleValue(text="L6 IT (VISp)",
                                 description="L6 IT (VISp)") )

class CellSetAliasAssigneeEnum(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="CellSetAliasAssigneeEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Bosiljka Tasic",
                PermissibleValue(text="Bosiljka Tasic",
                                 description="Bosiljka Tasic") )

class CellSetAliasCitationEnum(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="CellSetAliasCitationEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "10.1038/s41586-018-0654-5",
                PermissibleValue(text="10.1038/s41586-018-0654-5",
                                 description="10.1038/s41586-018-0654-5") )

class CuratedSynonymsEnum(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="CuratedSynonymsEnum",
    )

class ClassificationEnum(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="ClassificationEnum",
    )

class ClassificationCommentEnum(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="ClassificationCommentEnum",
    )

class ClassificationPubEnum(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="ClassificationPubEnum",
    )

class CLASSTYPEEnum(EnumDefinitionImpl):

    equivalent = PermissibleValue(text="equivalent",
                                           description="equivalent")

    _defn = EnumDefinition(
        name="CLASSTYPEEnum",
    )

# Slots
class slots:
    pass

slots.ID = Slot(uri=EXAMPLE.ID, name="ID", curie=EXAMPLE.curie('ID'),
                   model_uri=EXAMPLE.ID, domain=None, range=Optional[Union[str, AllenDendIdentifier]])

slots.Label = Slot(uri=EXAMPLE.Label, name="Label", curie=EXAMPLE.curie('Label'),
                   model_uri=EXAMPLE.Label, domain=None, range=Optional[str])

slots.PrefLabel = Slot(uri=EXAMPLE.PrefLabel, name="PrefLabel", curie=EXAMPLE.curie('PrefLabel'),
                   model_uri=EXAMPLE.PrefLabel, domain=None, range=Optional[str])

slots.Entity_Type = Slot(uri=EXAMPLE.Entity_Type, name="Entity Type", curie=EXAMPLE.curie('Entity_Type'),
                   model_uri=EXAMPLE.Entity_Type, domain=None, range=Optional[Union[str, BDSHELPIdentifier]])

slots.TYPE = Slot(uri=EXAMPLE.TYPE, name="TYPE", curie=EXAMPLE.curie('TYPE'),
                   model_uri=EXAMPLE.TYPE, domain=None, range=Optional[Union[str, "TYPEEnum"]])

slots.Property_Assertions = Slot(uri=EXAMPLE.Property_Assertions, name="Property Assertions", curie=EXAMPLE.curie('Property_Assertions'),
                   model_uri=EXAMPLE.Property_Assertions, domain=None, range=Optional[Union[str, AllenDendIdentifier]])

slots.Synonyms = Slot(uri=EXAMPLE.Synonyms, name="Synonyms", curie=EXAMPLE.curie('Synonyms'),
                   model_uri=EXAMPLE.Synonyms, domain=None, range=Optional[Union[str, List[str]]])

slots.Function = Slot(uri=EXAMPLE.Function, name="Function", curie=EXAMPLE.curie('Function'),
                   model_uri=EXAMPLE.Function, domain=None, range=Optional[Union[str, "FunctionEnum"]])

slots.cell_set_preferred_alias = Slot(uri=EXAMPLE.cell_set_preferred_alias, name="cell_set_preferred_alias", curie=EXAMPLE.curie('cell_set_preferred_alias'),
                   model_uri=EXAMPLE.cell_set_preferred_alias, domain=None, range=Optional[str])

slots.original_label = Slot(uri=EXAMPLE.original_label, name="original_label", curie=EXAMPLE.curie('original_label'),
                   model_uri=EXAMPLE.original_label, domain=None, range=Optional[str])

slots.cell_set_label = Slot(uri=EXAMPLE.cell_set_label, name="cell_set_label", curie=EXAMPLE.curie('cell_set_label'),
                   model_uri=EXAMPLE.cell_set_label, domain=None, range=Optional[str])

slots.cell_set_aligned_alias = Slot(uri=EXAMPLE.cell_set_aligned_alias, name="cell_set_aligned_alias", curie=EXAMPLE.curie('cell_set_aligned_alias'),
                   model_uri=EXAMPLE.cell_set_aligned_alias, domain=None, range=Optional[str])

slots.cell_set_additional_aliases = Slot(uri=EXAMPLE.cell_set_additional_aliases, name="cell_set_additional_aliases", curie=EXAMPLE.curie('cell_set_additional_aliases'),
                   model_uri=EXAMPLE.cell_set_additional_aliases, domain=None, range=Optional[Union[str, "CellSetAdditionalAliasesEnum"]])

slots.cell_set_alias_assignee = Slot(uri=EXAMPLE.cell_set_alias_assignee, name="cell_set_alias_assignee", curie=EXAMPLE.curie('cell_set_alias_assignee'),
                   model_uri=EXAMPLE.cell_set_alias_assignee, domain=None, range=Optional[Union[str, "CellSetAliasAssigneeEnum"]])

slots.cell_set_alias_citation = Slot(uri=EXAMPLE.cell_set_alias_citation, name="cell_set_alias_citation", curie=EXAMPLE.curie('cell_set_alias_citation'),
                   model_uri=EXAMPLE.cell_set_alias_citation, domain=None, range=Optional[Union[str, "CellSetAliasCitationEnum"]])

slots.Metadata = Slot(uri=EXAMPLE.Metadata, name="Metadata", curie=EXAMPLE.curie('Metadata'),
                   model_uri=EXAMPLE.Metadata, domain=None, range=Optional[Union[str, Identifier]])

slots.Synonyms_from_taxonomy = Slot(uri=EXAMPLE.Synonyms_from_taxonomy, name="Synonyms_from_taxonomy", curie=EXAMPLE.curie('Synonyms_from_taxonomy'),
                   model_uri=EXAMPLE.Synonyms_from_taxonomy, domain=None, range=Optional[Union[str, List[str]]])

slots.Curated_synonyms = Slot(uri=EXAMPLE.Curated_synonyms, name="Curated_synonyms", curie=EXAMPLE.curie('Curated_synonyms'),
                   model_uri=EXAMPLE.Curated_synonyms, domain=None, range=Optional[Union[str, "CuratedSynonymsEnum"]])

slots.Comment = Slot(uri=EXAMPLE.Comment, name="Comment", curie=EXAMPLE.curie('Comment'),
                   model_uri=EXAMPLE.Comment, domain=None, range=Optional[Union[str, CellSetPreferredAliasIdentifier]])

slots.Classification = Slot(uri=EXAMPLE.Classification, name="Classification", curie=EXAMPLE.curie('Classification'),
                   model_uri=EXAMPLE.Classification, domain=None, range=Optional[Union[str, "ClassificationEnum"]])

slots.Classification_comment = Slot(uri=EXAMPLE.Classification_comment, name="Classification_comment", curie=EXAMPLE.curie('Classification_comment'),
                   model_uri=EXAMPLE.Classification_comment, domain=None, range=Optional[Union[str, "ClassificationCommentEnum"]])

slots.Classification_pub = Slot(uri=EXAMPLE.Classification_pub, name="Classification_pub", curie=EXAMPLE.curie('Classification_pub'),
                   model_uri=EXAMPLE.Classification_pub, domain=None, range=Optional[Union[str, "ClassificationPubEnum"]])

slots.Exemplar = Slot(uri=EXAMPLE.Exemplar, name="Exemplar", curie=EXAMPLE.curie('Exemplar'),
                   model_uri=EXAMPLE.Exemplar, domain=None, range=Optional[Union[str, AllenDendIdentifier]])

slots.CLASS_TYPE = Slot(uri=EXAMPLE.CLASS_TYPE, name="CLASS_TYPE", curie=EXAMPLE.curie('CLASS_TYPE'),
                   model_uri=EXAMPLE.CLASS_TYPE, domain=None, range=Optional[Union[str, "CLASSTYPEEnum"]])

slots.Evidence = Slot(uri=EXAMPLE.Evidence, name="Evidence", curie=EXAMPLE.curie('Evidence'),
                   model_uri=EXAMPLE.Evidence, domain=None, range=Optional[Union[str, HttpIdentifier]])

slots.Gross_cell_type = Slot(uri=EXAMPLE.Gross_cell_type, name="Gross_cell_type", curie=EXAMPLE.curie('Gross_cell_type'),
                   model_uri=EXAMPLE.Gross_cell_type, domain=None, range=Optional[Union[str, CLIdentifier]])

slots.Brain_region = Slot(uri=EXAMPLE.Brain_region, name="Brain_region", curie=EXAMPLE.curie('Brain_region'),
                   model_uri=EXAMPLE.Brain_region, domain=None, range=Optional[Union[str, UBERONIdentifier]])

slots.Marker1 = Slot(uri=EXAMPLE.Marker1, name="Marker1", curie=EXAMPLE.curie('Marker1'),
                   model_uri=EXAMPLE.Marker1, domain=None, range=Optional[Union[str, EnsemblIdentifier]])

slots.Marker2 = Slot(uri=EXAMPLE.Marker2, name="Marker2", curie=EXAMPLE.curie('Marker2'),
                   model_uri=EXAMPLE.Marker2, domain=None, range=Optional[Union[str, EnsemblIdentifier]])

slots.Marker3 = Slot(uri=EXAMPLE.Marker3, name="Marker3", curie=EXAMPLE.curie('Marker3'),
                   model_uri=EXAMPLE.Marker3, domain=None, range=Optional[Union[str, EnsemblIdentifier]])

slots.Marker4 = Slot(uri=EXAMPLE.Marker4, name="Marker4", curie=EXAMPLE.curie('Marker4'),
                   model_uri=EXAMPLE.Marker4, domain=None, range=Optional[Union[str, EnsemblIdentifier]])

slots.Marker5 = Slot(uri=EXAMPLE.Marker5, name="Marker5", curie=EXAMPLE.curie('Marker5'),
                   model_uri=EXAMPLE.Marker5, domain=None, range=Optional[Union[str, EnsemblIdentifier]])

slots.Marker6 = Slot(uri=EXAMPLE.Marker6, name="Marker6", curie=EXAMPLE.curie('Marker6'),
                   model_uri=EXAMPLE.Marker6, domain=None, range=Optional[Union[str, EnsemblIdentifier]])

slots.Marker7 = Slot(uri=EXAMPLE.Marker7, name="Marker7", curie=EXAMPLE.curie('Marker7'),
                   model_uri=EXAMPLE.Marker7, domain=None, range=Optional[Union[str, EnsemblIdentifier]])

slots.Marker8 = Slot(uri=EXAMPLE.Marker8, name="Marker8", curie=EXAMPLE.curie('Marker8'),
                   model_uri=EXAMPLE.Marker8, domain=None, range=Optional[Union[str, EnsemblIdentifier]])

slots.Expresses = Slot(uri=EXAMPLE.Expresses, name="Expresses", curie=EXAMPLE.curie('Expresses'),
                   model_uri=EXAMPLE.Expresses, domain=None, range=Optional[Union[Union[str, EnsemblIdentifier], List[Union[str, EnsemblIdentifier]]]])

slots.Evidence_-_pub = Slot(uri=EXAMPLE['Evidence_-_pub'], name="Evidence - pub", curie=EXAMPLE.curie('Evidence_-_pub'),
                   model_uri=EXAMPLE['Evidence_-_pub'], domain=None, range=Optional[Union[str, DoiIdentifier]])

slots.Taxonomy_node_ID = Slot(uri=EXAMPLE.Taxonomy_node_ID, name="Taxonomy_node_ID", curie=EXAMPLE.curie('Taxonomy_node_ID'),
                   model_uri=EXAMPLE.Taxonomy_node_ID, domain=None, range=Optional[str])

slots.clusterName = Slot(uri=EXAMPLE.clusterName, name="clusterName", curie=EXAMPLE.curie('clusterName'),
                   model_uri=EXAMPLE.clusterName, domain=None, range=Optional[str])

slots.Markers_Delimited = Slot(uri=EXAMPLE.Markers_Delimited, name="Markers Delimited", curie=EXAMPLE.curie('Markers_Delimited'),
                   model_uri=EXAMPLE.Markers_Delimited, domain=None, range=Optional[Union[Union[str, EnsemblIdentifier], List[Union[str, EnsemblIdentifier]]]])

slots.NAME = Slot(uri=EXAMPLE.NAME, name="NAME", curie=EXAMPLE.curie('NAME'),
                   model_uri=EXAMPLE.NAME, domain=None, range=Optional[str])
