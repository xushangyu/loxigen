:: # Copyright 2013, Big Switch Networks, Inc.
:: #
:: # LoxiGen is licensed under the Eclipse Public License, version 1.0 (EPL), with
:: # the following special exception:
:: #
:: # LOXI Exception
:: #
:: # As a special exception to the terms of the EPL, you may distribute libraries
:: # generated by LoxiGen (LoxiGen Libraries) under the terms of your choice, provided
:: # that copyright and licensing notices generated by LoxiGen are not altered or removed
:: # from the LoxiGen Libraries and the notice provided below is (i) included in
:: # the LoxiGen Libraries, if distributed in source code form and (ii) included in any
:: # documentation for the LoxiGen Libraries, if distributed in binary form.
:: #
:: # Notice: "Copyright 2013, Big Switch Networks, Inc. This library was generated by the LoxiGen Compiler."
:: #
:: # You may not use this file except in compliance with the EPL or LOXI Exception. You may obtain
:: # a copy of the EPL at:
:: #
:: # http://www.eclipse.org/legal/epl-v10.html
:: #
:: # Unless required by applicable law or agreed to in writing, software
:: # distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
:: # WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
:: # EPL for the specific language governing permissions and limitations
:: # under the EPL.
::
:: import itertools
:: import of_g
:: include('_copyright.py')

:: include('_autogen.py')

import struct
import action
import const
import util
import loxi.generic_util
import loxi

def unpack_list(reader):
    def deserializer(reader, typ):
        parser = parsers.get(typ)
        if not parser: raise loxi.ProtocolError("unknown instruction type %d" % typ)
        return parser(reader)
    return loxi.generic_util.unpack_list_tlv16(reader, deserializer)

class Instruction(object):
    type = None # override in subclass
    pass

:: for ofclass in ofclasses:
:: include('_ofclass.py', ofclass=ofclass, superclass="Instruction")

:: #endfor

parsers = {
:: sort_key = lambda x: x.type_members[0].value
:: msgtype_groups = itertools.groupby(sorted(ofclasses, key=sort_key), sort_key)
:: for (k, v) in msgtype_groups:
:: v = list(v)
:: if len(v) == 1:
    ${k} : ${v[0].pyname}.unpack,
:: else:
    ${k} : parse_${k[12:].lower()},
:: #endif
:: #endfor
}
