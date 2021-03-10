# make -f seed.Makefile  src/schema/celltype.yaml 

TEMPLATEDIR = ../brain_data_standards_ontologies/src/templates

# TODO: ensure run in env
src/schema/celltype.yaml:
	python ~/repos/biolinkml/biolinkml/generators/infer_model.py tsvs2model -E CLASS_TYPE -E TYPE --robot $(TEMPLATEDIR)/*tsv > $@
