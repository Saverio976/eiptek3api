CMD_ARGS	?=	

all:
	uv run eiptek3api $(CMD_ARGS)

publish:
	uv build
	uv publish
