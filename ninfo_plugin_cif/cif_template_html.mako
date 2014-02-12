%if flat:
<table border="1" cellpadding="1" cellspacing="0">
<thead>
<tr>
    <th>Time First</th>
    <th>Time Last</th>
    <th>Address</th>
    <th>Confidence</th>
    <th>Assessment</th>
    <th>Description</th>
    <th>Portlist</th>
    <th>Alternative ID</th> 
</tr>
</thead>
<tbody>
%for r in flat:
<tr>
    <td> ${r['time_first']}     </td>
    <td> ${r['time_last']}      </td>
    <td> ${r['address']}        </td>
    <td> ${r['confidence']}        </td>
    <td> ${r['assessment']}     </td>
    <td> ${r['description']}    </td>
    <td> ${r.get('portlist','')}</td>
    <td> ${r['alternativeid']}  </td>
</tr>
%endfor
</tbody>
</table>
%endif
