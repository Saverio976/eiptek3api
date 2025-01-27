CMD_ARGS	?=	

all:
	uv run eiptek3api $(CMD_ARGS)

publish:
	rm -rf dist
	uv build
	uv publish
