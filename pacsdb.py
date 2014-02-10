#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (©) 2014 Marcel Ribeiro Dantas
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

import psycopg2
import sys

def numQueries(monthStart, monthEnd):
    cur.execute("""SELECT COUNT(*) FROM audit_record WHERE event_id_fk = 17 AND event_date_time >= DATE '%s' AND event_date_time < DATE '%s'""" % (monthStart, monthEnd))
    Queries = cur.fetchall()
    print "Número de solicitações: %s." % (Queries[0])

def numLogins(monthStart, monthEnd):
    cur.execute("""SELECT COUNT(*) FROM audit_record WHERE event_type_fk = 7 AND event_date_time >=  DATE '2013-12-01' AND event_date_time < DATE '2013-12-31'""")
    numberSuccessLogins = cur.fetchall()
    print "Número de logins realizados com sucesso: %s." % (numberSuccessLogins[0])

if __name__ == "__main__":
    try:
        conn_string = "host='pacs.lais.huol.ufrn.br' dbname='arrdb' user='jailton' password='password'"
        conn = psycopg2.connect(conn_string)
        cur = conn.cursor()
    except:
        print "\nNão foi possível conectar-se ao servidor.\n"
    print "Estatísticas de %s à %s" % (sys.argv[1], sys.argv[2])
    numQueries(sys.argv[1], sys.argv[2])
    numLogins(sys.argv[1], sys.argv[2])
