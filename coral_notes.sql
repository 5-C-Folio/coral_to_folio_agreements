SELECT r.titleText, rn.resourceID, case
					  when rn.noteTypeID = 17 then "Accessibility"
                      when rn.NoteTypeID = 3 then "Access Details"
                      when rn.NoteTypeID = 2 then "Acquisition Details"
                      when rn.NoteTypeID = 15 then "Data Integration"
                      when rn.NoteTypeID in (23,22,14,24) then "Discovery Details"
                      when rn.NoteTypeID in (4,1) then "General"
                      when rn.NoteTypeID = 5 then "Licensing Details"
                      when rn.NoteTypeID = 10 then "HLM"
                      when rn.NoteTypeId = 12 then "SFX"
                      else rn.NoteTypeID
                      end as "note Type",
rn.noteText

FROM coral_resources.ResourceNote rn
INNER JOIN coral_resources.NoteType nt
on rn.noteTypeID = nt.noteTypeID
inner join coral_resources.Resource r 
on r.resourceID = rn.ResourceID


WHERE rn.noteTypeID in (
17,
3,
2,
23,
22,
14,
24,
10,
5,
1,
12);
