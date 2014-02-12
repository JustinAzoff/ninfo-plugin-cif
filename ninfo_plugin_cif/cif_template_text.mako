%for r in flat:
${r['time_first']} - ${r['time_last']} ${r['address']} ${r['assessment']} ${r['description']} ${r.get('portlist','')} ${r['alternativeid']}
%endfor
