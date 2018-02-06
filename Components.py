

from InputComponent_Standing import *
from InputComponent_Jumping  import *

STANDING = "Standing"
JUMPING  = "Jumping"

InputComponent    = { STANDING : InputComponent_Standing,
		      JUMPING  : InputComponent_Jumping  }

from GraphicsComponent_Standing import *
from GraphicsComponent_Jumping  import *


GraphicsComponent    = { STANDING : GraphicsComponent_Standing,
		         JUMPING  : GraphicsComponent_Jumping  }


