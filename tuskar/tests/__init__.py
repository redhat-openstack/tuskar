# Copyright 2010 United States Government as represented by the
# Administrator of the National Aeronautics and Space Administration.
# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

"""
:mod:`Tuskar.tests` -- tuskar Unittests
=====================================================

.. automodule:: tuskar.tests
   :platform: Unix
"""

# TODO(deva): move eventlet imports to tuskar.__init__ once we move to PBR

import eventlet

eventlet.monkey_patch(os=False)

# See http://code.google.com/p/python-nose/issues/detail?id=373
# The code below enables nosetests to work with i18n _() blocks
import six.moves.builtins as __builtin__
setattr(__builtin__, '_', lambda x: x)
