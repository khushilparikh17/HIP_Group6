<?xml version='1.0' encoding='utf-8'?>
<scheme version="2.0" title="sleep" description="">
	<bookmarks>
		<bookmark x="null" y="null" />
		<bookmark x="null" y="null" />
		<bookmark x="null" y="null" />
		<bookmark x="null" y="null" />
		<bookmark x="null" y="null" />
		<bookmark x="null" y="null" />
		<bookmark x="null" y="null" />
		<bookmark x="null" y="null" />
		<bookmark x="null" y="null" />
		<bookmark x="null" y="null" />
	</bookmarks>
	<nodes>
		<node id="0" name="FFT Band-Pass Filter" qualified_name="widgets.spectral.owspectralselection.OWSpectralSelection" project_name="NeuroPype" version="1.0.0" title="FFT Band-Pass Filter&#10;[[0.5, 30] Hz]" uuid="00518325-1f71-4dd7-8d40-a1848b86d946" position="(1126.4677877066438, 304.92206212489776)" />
		<node id="1" name="Moving Window" qualified_name="widgets.signal_processing.owmovingwindow.OWMovingWindow" project_name="NeuroPype" version="1.1.0" title="Moving Window&#10;[30.0 seconds]" uuid="89924b11-481d-46e8-b8bb-8ca24d26669b" position="(1223.8819050216598, 382.2620206624607)" />
		<node id="2" name="Power Bands" qualified_name="widgets.spectral.owpowerbands.OWPowerBands" project_name="NeuroPype" version="1.4.0" title="Power Bands" uuid="6c13fcff-4b94-4e1f-8723-62548968bb55" position="(1024.9284195553414, 564.7025811442506)" />
		<node id="3" name="Bar Plot" qualified_name="widgets.visualization.owbarplot.OWBarPlot" project_name="NeuroPype" version="1.2.2" title="Bar Plot&#10;['[21_REM, Fpz_Cz] Band Power per 30-sec Epoch']" uuid="d73388b9-13a1-4e8e-9e65-fcd25a6f4572" position="(1166.0499922946901, 509.9750543530108)" />
		<node id="4" name="Fast Fourier Transform" qualified_name="widgets.spectral.owfastfouriertransform.OWFastFourierTransform" project_name="NeuroPype" version="1.0.0" title="Fast Fourier Transform&#10;[ backward norm. one-sided ]" uuid="82712b57-fe84-4671-bd68-4deea5fc3dce" position="(544.5053874058542, 572.8729195908113)" />
		<node id="5" name="Absolute Value" qualified_name="widgets.elementwise_math.owabsolute.OWAbsolute" project_name="NeuroPype" version="1.1.0" title="Absolute Value" uuid="35fb123e-9074-4e8b-9821-7c9cd039befb" position="(733.7159486581752, 568.5120206624608)" />
		<node id="6" name="Power (Exponentiate)" qualified_name="widgets.elementwise_math.owpower.OWPower" project_name="NeuroPype" version="1.1.0" title="Power (Exponentiate)&#10;[2.0]" uuid="9cfd9216-ddc5-4df1-92d5-0bb32d36735b" position="(898.8569593746709, 565.5076385793855)" />
		<node id="7" name="Select Range" qualified_name="widgets.tensor_math.owselectrange.OWSelectRange" project_name="NeuroPype" version="1.6.0" title="Select Range&#10;[['Fpz-Cz'] along named (default)]" uuid="bbc8ccea-5f2b-4254-bf69-05654191e935" position="(1019.5761614055546, 306.31632933770385)" />
		<node id="8" name="Import EDF" qualified_name="widgets.file_system.owimportedf.OWImportEDF" project_name="NeuroPype" version="2.1.0" title="Import EDF&#10;[C:/Users/user/Desktop/SC4052EC-Hypnogram.edf]" uuid="c4ec497f-4d30-4a8e-978d-f347aac305ff" position="(538.2458391816226, 86.78280549107262)" />
		<node id="9" name="Marker Stream Window" qualified_name="widgets.visualization.owmarkerstreamwindow.OWMarkerStreamWindow" project_name="NeuroPype" version="1.1.4" title="Marker Stream Window" uuid="efa04a2b-d7a5-4e69-ba09-96769cbfa037" position="(731.3756132937383, 77.50022126469821)" />
		<node id="10" name="Export Markers to CSV" qualified_name="widgets.markers.owexportmarkers.OWExportMarkers" project_name="NeuroPype" version="1.1.1" title="Export Markers to CSV" uuid="b1657953-dcb3-4ed7-ae08-ecc42607408e" position="(643.5686462137573, 114.68067072887334)" />
		<node id="11" name="Record to CSV" qualified_name="widgets.file_system.owrecordtocsv.OWRecordToCSV" project_name="NeuroPype" version="1.0.1" title="Record to CSV" uuid="56037bb1-aa1f-40e1-91fb-9cfceca8670b" position="(1172.6243094356578, 663.75)" />
		<node id="12" name="Parameter Port" qualified_name="widgets.programming.owparameterport.OWParameterPort" project_name="NeuroPype" version="1.3.4" title="Parameter Port&#10;[data (C:/Users/user/Desktop/SC4021E0-PSG.edf) (str)]" uuid="fa079d1e-a718-462e-a1c3-bd4142604198" position="(542.4391304347826, 306.9521739130435)" />
		<node id="13" name="Import EDF" qualified_name="widgets.file_system.owimportedf.OWImportEDF" project_name="NeuroPype" version="2.1.0" title="Import EDF&#10;[]" uuid="3acc92bf-9004-4149-8c60-8053fcd8737e" position="(631.1108695652174, 306.95217391304345)" />
		<node id="14" name="Stream Data" qualified_name="widgets.formatting.owstreamdata.OWStreamData" project_name="NeuroPype" version="1.3.0" title="Stream Data&#10;[wallclock timing, looping, 5.0% jitter, start pos 21870.0s]" uuid="6b5599fc-d0f2-4017-a83f-c776a0383e04" position="(830.0795460221766, 305.70217391304345)" />
		<node id="15" name="Dejitter Timestamps" qualified_name="widgets.utilities.owdejittertimestamps.OWDejitterTimestamps" project_name="NeuroPype" version="1.0.0" title="Dejitter Timestamps" uuid="40165ca7-d133-4d9a-8ab0-2bfd237bf39e" position="(926.3630434782608, 306.9608695652174)" />
		<node id="16" name="Separate Streams" qualified_name="widgets.formatting.owseparatestreams.OWSeparateStreams" project_name="NeuroPype" version="0.5.0" title="Separate Streams&#10;[modality=='EEG']" uuid="7d130a6b-d6e3-411e-b1e5-fa4cb32e2778" position="(726.1804347826087, 308.2108695652174)" />
	</nodes>
	<links>
		<link id="0" source_node_id="0" sink_node_id="1" source_channel="Data" sink_channel="Data" enabled="true" />
		<link id="1" source_node_id="4" sink_node_id="5" source_channel="Data" sink_channel="Data" enabled="true" />
		<link id="2" source_node_id="5" sink_node_id="6" source_channel="Data" sink_channel="Data" enabled="true" />
		<link id="3" source_node_id="6" sink_node_id="2" source_channel="Data" sink_channel="Data" enabled="true" />
		<link id="4" source_node_id="7" sink_node_id="0" source_channel="Data" sink_channel="Data" enabled="true" />
		<link id="5" source_node_id="8" sink_node_id="9" source_channel="Data" sink_channel="Data" enabled="false" />
		<link id="6" source_node_id="8" sink_node_id="10" source_channel="Data" sink_channel="Data" enabled="true" />
		<link id="7" source_node_id="12" sink_node_id="13" source_channel="Value" sink_channel="Filename" enabled="true" />
		<link id="8" source_node_id="14" sink_node_id="15" source_channel="Data" sink_channel="Data" enabled="true" />
		<link id="9" source_node_id="15" sink_node_id="7" source_channel="Data" sink_channel="Data" enabled="true" />
		<link id="10" source_node_id="13" sink_node_id="16" source_channel="Data" sink_channel="Data" enabled="true" />
		<link id="11" source_node_id="16" sink_node_id="14" source_channel="Matching" sink_channel="Data" enabled="true" />
		<link id="12" source_node_id="1" sink_node_id="4" source_channel="Data" sink_channel="Data" enabled="true" />
		<link id="13" source_node_id="2" sink_node_id="3" source_channel="Data" sink_channel="Data" enabled="true" />
		<link id="14" source_node_id="2" sink_node_id="11" source_channel="Data" sink_channel="Data" enabled="true" />
	</links>
	<annotations>
		<text id="0" rect="(791.25, 59.5, 297.5, 50.0)" font-family="DejaVu Sans Mono" font-size="16">1. Get the markers to determine the strat pos</text>
		<text id="1" rect="(768.050540161717, 212.62174207847409, 268.32247359491316, 88.0)" font-family="DejaVu Sans Mono" font-size="16">2. Adjust 'Start Pos' based on markers</text>
	</annotations>
	<thumbnail />
	<node_properties>
		<properties node_id="0" format="pickle">gASVKQEAAAAAAAB9lCiMCWJsb2Nrc2l6ZZRLZIwIZmZ0X3NpemWUjA0odXNlIGRlZmF1bHQplIwL
ZnJlcXVlbmNpZXOUXZQoRz/gAAAAAAAASx5ljAZsZWdhY3mUiYwIbWV0YWRhdGGUfZSME3NhdmVk
V2lkZ2V0R2VvbWV0cnmUjAlQeVF0Ni5zaXCUjA5fdW5waWNrbGVfdHlwZZSTlIwMUHlRdDYuUXRD
b3JllIwKUUJ5dGVBcnJheZRDQgHZ0MsAAwAAAAABswAAAH4AAAM4AAACIAAAAbMAAACcAAADOAAA
AiAAAAAAAAAAAAUAAAABswAAAJwAAAM4AAACIJSFlIeUUpSMDnNldF9icmVha3BvaW50lImMDXN0
b3BiYW5kX2dhaW6URwAAAAAAAAAAdS4=
</properties>
		<properties node_id="1" format="pickle">gASVCAEAAAAAAAB9lCiMD2ZsYWdfYXNfb2ZmbGluZZSJjAhtZXRhZGF0YZR9lIwTc2F2ZWRXaWRn
ZXRHZW9tZXRyeZSMCVB5UXQ2LnNpcJSMDl91bnBpY2tsZV90eXBllJOUjAxQeVF0Ni5RdENvcmWU
jApRQnl0ZUFycmF5lENCAdnQywADAAAAAAJrAAAAmgAAA/oAAAIBAAACawAAALgAAAP6AAACAQAA
AAAAAAAABQAAAAJrAAAAuAAAA/oAAAIBlIWUh5RSlIwOc2V0X2JyZWFrcG9pbnSUiYwEdW5pdJSM
B3NlY29uZHOUjAd2ZXJib3NllImMDXdpbmRvd19sZW5ndGiUR0A+AAAAAAAAdS4=
</properties>
		<properties node_id="2" format="pickle">gASVnAEAAAAAAAB9lCiMBWFscGhhlF2UKEsISw1ljBdhdmVyYWdlX2Fjcm9zc19jaGFubmVsc5SJ
jARiZXRhlF2UKEsNSx5ljBNjb3JyZWN0X2Zvcl9mYWxsb2ZmlIiMDGN1c3RvbV9iYW5kc5R9lIwF
ZGVsdGGUXZQoRz/gAAAAAAAASwRljAVnYW1tYZRdlChLHksoZYwaa2VlcF9udW1lcmljX2JhbmRf
aW5fbmFtZXOUiYwJbWVhbl90cmltlH2UjAhtZXRhZGF0YZR9lIwTc2F2ZWRXaWRnZXRHZW9tZXRy
eZSMCVB5UXQ2LnNpcJSMDl91bnBpY2tsZV90eXBllJOUjAxQeVF0Ni5RdENvcmWUjApRQnl0ZUFy
cmF5lENCAdnQywADAAAAAAJnAAAAHwAAA84AAAKwAAACZwAAAD0AAAPOAAACsAAAAAAAAAAABQAA
AAJnAAAAPQAAA84AAAKwlIWUh5RSlIwOc2V0X2JyZWFrcG9pbnSUiYwFdGhldGGUXZQoSwRLCGWM
BHVuaXSUjAJkQpSMB3ZlcmJvc2WUiHUu
</properties>
		<properties node_id="3" format="pickle">gASVNwMAAAAAAAB9lCiMDWFsd2F5c19vbl90b3CUiYwUYW5ub3RhdGlvbl9mb250X3NpemWUR0Am
AAAAAAAAjAthbnRpYWxpYXNlZJSIjBBhdXRvX2xpbmVfY29sb3JzlIiMBGF4aXOUjAdmZWF0dXJl
lIwQYmFja2dyb3VuZF9jb2xvcpSMByMzMDMwMzCUjAhjb2xvcm1hcJSMDGdpc3RfcmFpbmJvd5SM
EGRlY29yYXRpb25fY29sb3KUjAcjQjBCMEIwlIwJZm9udF9zaXpllEdAJgAAAAAAAIwMaW5pdGlh
bF9kaW1zlF2UKEsySzJN6ANNIANljA5pbnN0YW5jZV9maWVsZJSMDSh1c2UgZGVmYXVsdCmUjA5s
YWJlbF9yb3RhdGlvbpSMCmhvcml6b250YWyUjAtsZWZ0X29mZnNldJRLAIwKbGluZV9jb2xvcpSM
BXdoaXRllIwKbGluZV93aWR0aJRHP+mZmZmZmZqMDG1heF9jaGFubmVsc5RLBIwIbWV0YWRhdGGU
fZSMC3Bsb3RfbWlubWF4lImME3NhdmVkV2lkZ2V0R2VvbWV0cnmUjAlQeVF0Ni5zaXCUjA5fdW5w
aWNrbGVfdHlwZZSTlIwMUHlRdDYuUXRDb3JllIwKUUJ5dGVBcnJheZRDQgHZ0MsAAwAAAAACdgAA
AAAAAAPdAAACswAAAnYAAAAeAAAD3QAAArMAAAAAAAAAAAUAAAACdgAAAB4AAAPdAAACs5SFlIeU
UpSMDnNldF9icmVha3BvaW50lImMDHNob3dfdG9vbGJhcpSJjAZzdHJlYW2UaBGMC3N0cmVhbV9u
YW1llGgRjAx0aWdodF9sYXlvdXSUiIwFdGl0bGWUjCxbMjFfUkVNLCBGcHpfQ3pdIEJhbmQgUG93
ZXIgcGVyIDMwLXNlYyBFcG9jaJSMFXRyYWNrX3dpbmRvd19wb3NpdGlvbpSJjAd2ZXJib3NllImM
B3hfbGFiZWyUjA5GcmVxdWVuY3kgYmFuZJSMB3lfbGFiZWyUjApQb3dlciAoZEIplIwIeV9saW1p
dHOUXZQoSwBLZGWMCnplcm9fY29sb3KUjAcjNjA2MDYwlHUu
</properties>
		<properties node_id="4" format="pickle">gASVOAEAAAAAAAB9lCiMBGF4aXOUjAR0aW1llIwIbWV0YWRhdGGUfZSMAW6UjA0odXNlIGRlZmF1
bHQplIwNbm9ybWFsaXphdGlvbpSMCGJhY2t3YXJklIwObnVtX3BhcnRpdGlvbnOUSwSMCG9uZXNp
ZGVklIiMDnBhcnRpdGlvbl9heGlzlIwIZGlzYWJsZWSUjBNzYXZlZFdpZGdldEdlb21ldHJ5lIwJ
UHlRdDYuc2lwlIwOX3VucGlja2xlX3R5cGWUk5SMDFB5UXQ2LlF0Q29yZZSMClFCeXRlQXJyYXmU
Q0IB2dDLAAMAAAAAAkwAAAB7AAADswAAAkMAAAJMAAAAmQAAA7MAAAJDAAAAAAAAAAAFAAAAAkwA
AACZAAADswAAAkOUhZSHlFKUjA5zZXRfYnJlYWtwb2ludJSJdS4=
</properties>
		<properties node_id="5" format="pickle">gASVwAAAAAAAAAB9lCiMCG1ldGFkYXRhlH2UjBNzYXZlZFdpZGdldEdlb21ldHJ5lIwJUHlRdDYu
c2lwlIwOX3VucGlja2xlX3R5cGWUk5SMDFB5UXQ2LlF0Q29yZZSMClFCeXRlQXJyYXmUQ0IB2dDL
AAMAAAAAAcIAAAD+AAADKQAAAZ8AAAHCAAABHAAAAykAAAGfAAAAAAAAAAAFAAAAAcIAAAEcAAAD
KQAAAZ+UhZSHlFKUjA5zZXRfYnJlYWtwb2ludJSJdS4=
</properties>
		<properties node_id="6" format="pickle">gASV0QAAAAAAAAB9lCiMCG1ldGFkYXRhlH2UjAVwb3dlcpRHQAAAAAAAAACME3NhdmVkV2lkZ2V0
R2VvbWV0cnmUjAlQeVF0Ni5zaXCUjA5fdW5waWNrbGVfdHlwZZSTlIwMUHlRdDYuUXRDb3JllIwK
UUJ5dGVBcnJheZRDQgHZ0MsAAwAAAAABwgAAAN0AAAMpAAABwQAAAcIAAAD7AAADKQAAAcEAAAAA
AAAAAAUAAAABwgAAAPsAAAMpAAABwZSFlIeUUpSMDnNldF9icmVha3BvaW50lIl1Lg==
</properties>
		<properties node_id="7" format="pickle">gASVYgEAAAAAAAB9lCiME2FwcGx5X211bHRpcGxlX2F4ZXOUiYwfYXBwbHlfdGltZV9zZWxlY3Rp
b25fdG9fbWFya2Vyc5SJjARheGlzlIwFbmFtZWSUjBBkcm9wX2lmX25vbnJhbmdllIwGbGVnYWN5
lIwQaW52ZXJ0X3NlbGVjdGlvbpSJjAhtZXRhZGF0YZR9lIwTc2F2ZWRXaWRnZXRHZW9tZXRyeZSM
CVB5UXQ2LnNpcJSMDl91bnBpY2tsZV90eXBllJOUjAxQeVF0Ni5RdENvcmWUjApRQnl0ZUFycmF5
lENCAdnQywADAAAAAAGoAAAAWgAAA0MAAAJEAAABqAAAAHgAAANDAAACRAAAAAAAAAAABQAAAAGo
AAAAeAAAA0MAAAJElIWUh5RSlIwJc2VsZWN0aW9ulF2UjAZGcHotQ3qUYYwOc2V0X2JyZWFrcG9p
bnSUiYwEdW5pdJSMB2RlZmF1bHSUdS4=
</properties>
		<properties node_id="8" format="pickle">gASVnAEAAAAAAAB9lCiMDWNsb3VkX2FjY291bnSUjA0odXNlIGRlZmF1bHQplIwMY2xvdWRfYnVj
a2V0lGgCjBFjbG91ZF9jcmVkZW50aWFsc5RoAowKY2xvdWRfaG9zdJSMB0RlZmF1bHSUjBBleGNs
dWRlX2NoYW5uZWxzlF2UjAhmaWxlbmFtZZSMLEM6L1VzZXJzL3VzZXIvRGVza3RvcC9TQzQwNTJF
Qy1IeXBub2dyYW0uZWRmlIwIbWV0YWRhdGGUfZSME3NhdmVkV2lkZ2V0R2VvbWV0cnmUjAlQeVF0
Ni5zaXCUjA5fdW5waWNrbGVfdHlwZZSTlIwMUHlRdDYuUXRDb3JllIwKUUJ5dGVBcnJheZRDQgHZ
0MsAAwAAAAABwgAAAC0AAAMpAAACcQAAAcIAAABLAAADKQAAAnEAAAAAAAAAAAUAAAABwgAAAEsA
AAMpAAACcZSFlIeUUpSMDnNldF9icmVha3BvaW50lImMDHN0aW1fY2hhbm5lbJRoAowOc3RyaXBf
bW9kYWxpdHmUiIwEdW5pdJSMAnVWlHUu
</properties>
		<properties node_id="9" format="pickle">gASVRQEAAAAAAAB9lCiMDWFsd2F5c19vbl90b3CUiYwMaW5pdGlhbF9kaW1zlF2UKEsySzJN9AFN
9AFljAhtZXRhZGF0YZR9lIwOb3ZlcnJpZGVfc3JhdGWUjA0odXNlIGRlZmF1bHQplIwTc2F2ZWRX
aWRnZXRHZW9tZXRyeZSMCVB5UXQ2LnNpcJSMDl91bnBpY2tsZV90eXBllJOUjAxQeVF0Ni5RdENv
cmWUjApRQnl0ZUFycmF5lENCAdnQywADAAAAAANiAAAAiQAABMkAAAJJAAADYgAAAKcAAATJAAAC
SQAAAAAAAAAABQAAAANiAAAApwAABMkAAAJJlIWUh5RSlIwOc2V0X2JyZWFrcG9pbnSUiYwGc3Ry
ZWFtlIwHbWFya2Vyc5SMC3N0cmVhbV9uYW1llIwHbWFya2Vyc5SMB3ZlcmJvc2WUiHUu
</properties>
		<properties node_id="10" format="pickle">gASVeAEAAAAAAAB9lCiMDWNsb3VkX2FjY291bnSUjA0odXNlIGRlZmF1bHQplIwMY2xvdWRfYnVj
a2V0lGgCjBFjbG91ZF9jcmVkZW50aWFsc5RoAowKY2xvdWRfaG9zdJSMB0RlZmF1bHSUjAhmaWxl
bmFtZZSMC21hcmtlcnMuY3N2lIwIbWV0YWRhdGGUfZSMC291dHB1dF9yb290lIwdQzovVXNlcnMv
dXNlci9EZXNrdG9wL21hcmtlcnOUjBNzYXZlZFdpZGdldEdlb21ldHJ5lIwJUHlRdDYuc2lwlIwO
X3VucGlja2xlX3R5cGWUk5SMDFB5UXQ2LlF0Q29yZZSMClFCeXRlQXJyYXmUQ0IB2dDLAAMAAAAA
AvUAAACpAAAEXAAAAmgAAAL1AAAAxwAABFwAAAJoAAAAAAAAAAAFAAAAAvUAAADHAAAEXAAAAmiU
hZSHlFKUjA5zZXRfYnJlYWtwb2ludJSJjAZzdHJlYW2UjAdtYXJrZXJzlHUu
</properties>
		<properties node_id="11" format="pickle">gASV4gEAAAAAAAB9lCiMF2Fic29sdXRlX2luc3RhbmNlX3RpbWVzlIiMDWNsb3VkX2FjY291bnSU
jA0odXNlIGRlZmF1bHQplIwMY2xvdWRfYnVja2V0lGgDjBFjbG91ZF9jcmVkZW50aWFsc5RoA4wK
Y2xvdWRfaG9zdJSMB0RlZmF1bHSUjA1jb2x1bW5faGVhZGVylIiMDGRlbGV0ZV9wYXJ0c5SIjAhm
aWxlbmFtZZSMETIxX1JFTV9GcHpfQ3ouY3N2lIwIbWV0YWRhdGGUfZSMC291dHB1dF9yb290lIwc
QzovVXNlcnMvdXNlci9EZXNrdG9wL0Zwei1DepSMC3JldHJpZXZhYmxllImME3NhdmVkV2lkZ2V0
R2VvbWV0cnmUjAlQeVF0Ni5zaXCUjA5fdW5waWNrbGVfdHlwZZSTlIwMUHlRdDYuUXRDb3JllIwK
UUJ5dGVBcnJheZRDQgHZ0MsAAwAAAAACkwAAAAkAAAP6AAACsAAAApMAAAAnAAAD+gAAArAAAAAA
AAAAAAUAAAACkwAAACcAAAP6AAACsJSFlIeUUpSMDnNldF9icmVha3BvaW50lImMC3RpbWVfc3Rh
bXBzlIiMD3RpbWVzdGFtcF9sYWJlbJSMCXRpbWVzdGFtcJR1Lg==
</properties>
		<properties node_id="12" format="pickle">gASV9QEAAAAAAAB9lCiMCGF1dG9jYXN0lIiMCWNhbmJlbm9uZZSIjAdkZWZhdWx0lIwmQzovVXNl
cnMvdXNlci9EZXNrdG9wL1NDNDAyMUUwLVBTRy5lZGaUjARkZXNjlIwNKHVzZSBkZWZhdWx0KZSM
BmRvbWFpbpRoBowIZWRpdGFibGWUiIwGZXhwZXJ0lImMC2lzX2ZpbGVuYW1llImMCmlzX3Zpc2li
bGWUiIwIbWV0YWRhdGGUfZSMDXBvcnRfY2F0ZWdvcnmUaAaMCHBvcnRuYW1llIwEZGF0YZSMDXJl
bGF0aW9uc2hpcHOUXZSMBHNhZmWUiYwTc2F2ZWRXaWRnZXRHZW9tZXRyeZSMCVB5UXQ2LnNpcJSM
Dl91bnBpY2tsZV90eXBllJOUjAxQeVF0Ni5RdENvcmWUjApRQnl0ZUFycmF5lENCAdnQywADAAAA
AAGsAAAAAAAAA0AAAAKzAAABrAAAAB4AAANAAAACswAAAAAAAAAABQAAAAGsAAAAHgAAA0AAAAKz
lIWUh5RSlIwGc2VsZWN0lIwEbm9uZZSME3NlbmRfc2lnbmFsX2NoYW5nZWSUiIwOc2V0X2JyZWFr
cG9pbnSUiYwKdmFsdWVfdHlwZZSMA3N0cpSMB3ZlcmJvc2WUiYwMdmVyYm9zZV9uYW1llGgGdS4=
</properties>
		<properties node_id="13" format="pickle">gASVwAEAAAAAAAB9lCiMDWNsb3VkX2FjY291bnSUjA0odXNlIGRlZmF1bHQplIwMY2xvdWRfYnVj
a2V0lGgCjBFjbG91ZF9jcmVkZW50aWFsc5RoAowKY2xvdWRfaG9zdJSMB0RlZmF1bHSUjBBleGNs
dWRlX2NoYW5uZWxzlF2UKIwORU9HIGhvcml6b250YWyUjA5SZXNwIG9yby1uYXNhbJSMDUVNRyBz
dWJtZW50YWyUjAtUZW1wIHJlY3RhbJSMDEV2ZW50IG1hcmtlcpRljAhmaWxlbmFtZZRoAowIbWV0
YWRhdGGUfZSME3NhdmVkV2lkZ2V0R2VvbWV0cnmUjAlQeVF0Ni5zaXCUjA5fdW5waWNrbGVfdHlw
ZZSTlIwMUHlRdDYuUXRDb3JllIwKUUJ5dGVBcnJheZRDQgHZ0MsAAwAAAAABwgAAAC0AAAMpAAAC
cQAAAcIAAABLAAADKQAAAnEAAAAAAAAAAAUAAAABwgAAAEsAAAMpAAACcZSFlIeUUpSMDnNldF9i
cmVha3BvaW50lImMDHN0aW1fY2hhbm5lbJRoAowOc3RyaXBfbW9kYWxpdHmUiIwEdW5pdJSMAnVW
lHUu
</properties>
		<properties node_id="14" format="pickle">gASV3QEAAAAAAAB9lCiMCmRhdGFfZHR5cGWUjAdmbG9hdDY0lIwUZGF0YV9yYW5nZV90b19zdHJl
YW2UjAtsZWdhY3ktd2FybpSMEWhpdGNoX3Byb2JhYmlsaXR5lEcAAAAAAAAAAIwOaml0dGVyX3Bl
cmNlbnSUR0AUAAAAAAAAjAxsb2dfcHJvZ3Jlc3OUiYwHbG9vcGluZ5SIjAhtZXRhZGF0YZR9lIwI
cmFuZHNlZWSUjA0odXNlIGRlZmF1bHQplIwTc2F2ZWRXaWRnZXRHZW9tZXRyeZSMCVB5UXQ2LnNp
cJSMDl91bnBpY2tsZV90eXBllJOUjAxQeVF0Ni5RdENvcmWUjApRQnl0ZUFycmF5lENCAdnQywAD
AAAAAAKBAAAAAAAABP0AAALOAAACgQAAAB4AAAT9AAACzgAAAAAAAAAABQAAAAKBAAAAHgAABP0A
AALOlIWUh5RSlIwOc2V0X2JyZWFrcG9pbnSUiYwHc3BlZWR1cJRHP/AAAAAAAACMCXN0YXJ0X3Bv
c5RHQNVbgAAAAACMEHRpbWVzdGFtcF9qaXR0ZXKURwAAAAAAAAAAjAZ0aW1pbmeUjAl3YWxsY2xv
Y2uUjA91cGRhdGVfaW50ZXJ2YWyURz+keuFHrhR7dS4=
</properties>
		<properties node_id="15" format="pickle">gASVGAEAAAAAAAB9lCiMD2ZvcmNlX21vbm90b25pY5SIjA9mb3JnZXRfaGFsZnRpbWWUR0BWgAAA
AAAAjA5tYXhfdXBkYXRlcmF0ZZRN9AGMCG1ldGFkYXRhlH2UjBNzYXZlZFdpZGdldEdlb21ldHJ5
lIwJUHlRdDYuc2lwlIwOX3VucGlja2xlX3R5cGWUk5SMDFB5UXQ2LlF0Q29yZZSMClFCeXRlQXJy
YXmUQ0IB2dDLAAMAAAAAAb0AAACfAAADLwAAAf4AAAG9AAAAvQAAAy8AAAH+AAAAAAAAAAAFAAAA
Ab0AAAC9AAADLwAAAf6UhZSHlFKUjA5zZXRfYnJlYWtwb2ludJSJjA53YXJtdXBfc2FtcGxlc5RK
/////3Uu
</properties>
		<properties node_id="16" format="pickle">gASV3gAAAAAAAAB9lCiMCWNvbmRpdGlvbpSMD21vZGFsaXR5PT0nRUVHJ5SMCG1ldGFkYXRhlH2U
jBNzYXZlZFdpZGdldEdlb21ldHJ5lIwJUHlRdDYuc2lwlIwOX3VucGlja2xlX3R5cGWUk5SMDFB5
UXQ2LlF0Q29yZZSMClFCeXRlQXJyYXmUQ0IB2dDLAAMAAAAAAcIAAADbAAADKQAAAcMAAAHCAAAA
+QAAAykAAAHDAAAAAAAAAAAFAAAAAcIAAAD5AAADKQAAAcOUhZSHlFKUjA5zZXRfYnJlYWtwb2lu
dJSJdS4=
</properties>
	</node_properties>
	<patch>{"description": {"description": "", "license": "", "name": "sleep", "status": "(unspecified)", "url": "", "version": "0.0.0"}, "edges": [["node1", "data", "node2", "data"], ["node5", "data", "node6", "data"], ["node6", "data", "node7", "data"], ["node7", "data", "node3", "data"], ["node8", "data", "node1", "data"], ["node9", "data", "node11", "data"], ["node13", "value", "node14", "filename"], ["node15", "data", "node16", "data"], ["node16", "data", "node8", "data"], ["node14", "data", "node17", "data"], ["node17", "matching", "node15", "data"], ["node2", "data", "node5", "data"], ["node3", "data", "node4", "data"], ["node3", "data", "node12", "data"]], "nodes": {"node1": {"class": "SpectralSelection", "module": "neuropype.nodes.spectral.SpectralSelection", "params": {"blocksize": {"customized": false, "type": "IntPort", "value": 100}, "fft_size": {"customized": false, "type": "IntPort", "value": null}, "frequencies": {"customized": true, "type": "ListPort", "value": [0.5, 30]}, "legacy": {"customized": false, "type": "BoolPort", "value": false}, "metadata": {"customized": false, "type": "DictPort", "value": {}}, "set_breakpoint": {"customized": false, "type": "BoolPort", "value": false}, "stopband_gain": {"customized": false, "type": "FloatPort", "value": 0.0}}, "uuid": "00518325-1f71-4dd7-8d40-a1848b86d946"}, "node10": {"class": "MarkerStreamWindow", "module": "neuropype.nodes.visualization.MarkerStreamWindow", "params": {"always_on_top": {"customized": false, "type": "BoolPort", "value": false}, "initial_dims": {"customized": false, "type": "ListPort", "value": [50, 50, 500, 500]}, "metadata": {"customized": false, "type": "DictPort", "value": {}}, "override_srate": {"customized": false, "type": "FloatPort", "value": null}, "set_breakpoint": {"customized": false, "type": "BoolPort", "value": false}, "stream": {"customized": false, "type": "StringPort", "value": "markers"}, "stream_name": {"customized": true, "type": "AliasPort", "value": "markers"}, "verbose": {"customized": false, "type": "BoolPort", "value": true}}, "uuid": "efa04a2b-d7a5-4e69-ba09-96769cbfa037"}, "node11": {"class": "ExportMarkers", "module": "neuropype.nodes.markers.ExportMarkers", "params": {"cloud_account": {"customized": false, "type": "StringPort", "value": ""}, "cloud_bucket": {"customized": false, "type": "StringPort", "value": ""}, "cloud_credentials": {"customized": false, "type": "StringPort", "value": ""}, "cloud_host": {"customized": false, "type": "EnumPort", "value": "Default"}, "filename": {"customized": true, "type": "StringPort", "value": "markers.csv"}, "metadata": {"customized": false, "type": "DictPort", "value": {}}, "output_root": {"customized": true, "type": "StringPort", "value": "C:/Users/user/Desktop/markers"}, "set_breakpoint": {"customized": false, "type": "BoolPort", "value": false}, "stream": {"customized": true, "type": "StringPort", "value": "markers"}}, "uuid": "b1657953-dcb3-4ed7-ae08-ecc42607408e"}, "node12": {"class": "RecordToCSV", "module": "neuropype.nodes.file_system.RecordToCSV", "params": {"absolute_instance_times": {"customized": false, "type": "BoolPort", "value": true}, "cloud_account": {"customized": false, "type": "StringPort", "value": ""}, "cloud_bucket": {"customized": false, "type": "StringPort", "value": ""}, "cloud_credentials": {"customized": false, "type": "StringPort", "value": ""}, "cloud_host": {"customized": false, "type": "EnumPort", "value": "Default"}, "column_header": {"customized": false, "type": "BoolPort", "value": true}, "delete_parts": {"customized": false, "type": "BoolPort", "value": true}, "filename": {"customized": true, "type": "StringPort", "value": "21_REM_Fpz_Cz.csv"}, "metadata": {"customized": false, "type": "DictPort", "value": {}}, "output_root": {"customized": true, "type": "StringPort", "value": "C:/Users/user/Desktop/Fpz-Cz"}, "retrievable": {"customized": false, "type": "BoolPort", "value": false}, "set_breakpoint": {"customized": false, "type": "BoolPort", "value": false}, "time_stamps": {"customized": false, "type": "BoolPort", "value": true}, "timestamp_label": {"customized": false, "type": "StringPort", "value": "timestamp"}}, "uuid": "56037bb1-aa1f-40e1-91fb-9cfceca8670b"}, "node13": {"class": "ParameterPort", "module": "neuropype.nodes.programming.ParameterPort", "params": {"autocast": {"customized": false, "type": "BoolPort", "value": true}, "canbenone": {"customized": false, "type": "BoolPort", "value": true}, "default": {"customized": true, "type": "Port", "value": "C:/Users/user/Desktop/SC4021E0-PSG.edf"}, "desc": {"customized": false, "type": "StringPort", "value": ""}, "domain": {"customized": false, "type": "Port", "value": null}, "editable": {"customized": false, "type": "BoolPort", "value": true}, "expert": {"customized": false, "type": "BoolPort", "value": false}, "is_filename": {"customized": false, "type": "BoolPort", "value": false}, "is_visible": {"customized": false, "type": "BoolPort", "value": true}, "metadata": {"customized": false, "type": "DictPort", "value": {}}, "port_category": {"customized": false, "type": "StringPort", "value": ""}, "portname": {"customized": false, "type": "StringPort", "value": "data"}, "relationships": {"customized": false, "type": "ListPort", "value": []}, "safe": {"customized": false, "type": "BoolPort", "value": false}, "select": {"customized": false, "type": "EnumPort", "value": "none"}, "send_signal_changed": {"customized": false, "type": "BoolPort", "value": true}, "set_breakpoint": {"customized": false, "type": "BoolPort", "value": false}, "value_type": {"customized": false, "type": "EnumPort", "value": "str"}, "verbose": {"customized": false, "type": "BoolPort", "value": false}, "verbose_name": {"customized": false, "type": "StringPort", "value": null}}, "uuid": "fa079d1e-a718-462e-a1c3-bd4142604198"}, "node14": {"class": "ImportEDF", "module": "neuropype.nodes.file_system.ImportEDF", "params": {"cloud_account": {"customized": false, "type": "StringPort", "value": ""}, "cloud_bucket": {"customized": false, "type": "StringPort", "value": ""}, "cloud_credentials": {"customized": false, "type": "StringPort", "value": ""}, "cloud_host": {"customized": false, "type": "EnumPort", "value": "Default"}, "exclude_channels": {"customized": true, "type": "ListPort", "value": ["EOG horizontal", "Resp oro-nasal", "EMG submental", "Temp rectal", "Event marker"]}, "filename": {"customized": false, "type": "StringPort", "value": ""}, "metadata": {"customized": false, "type": "DictPort", "value": {}}, "set_breakpoint": {"customized": false, "type": "BoolPort", "value": false}, "stim_channel": {"customized": false, "type": "StringPort", "value": ""}, "strip_modality": {"customized": false, "type": "BoolPort", "value": true}, "unit": {"customized": false, "type": "EnumPort", "value": "uV"}}, "uuid": "3acc92bf-9004-4149-8c60-8053fcd8737e"}, "node15": {"class": "StreamData", "module": "neuropype.nodes.formatting.StreamData", "params": {"data_dtype": {"customized": false, "type": "EnumPort", "value": "float64"}, "data_range_to_stream": {"customized": false, "type": "EnumPort", "value": "legacy-warn"}, "hitch_probability": {"customized": false, "type": "FloatPort", "value": 0.0}, "jitter_percent": {"customized": false, "type": "FloatPort", "value": 5.0}, "log_progress": {"customized": false, "type": "BoolPort", "value": false}, "looping": {"customized": false, "type": "BoolPort", "value": true}, "metadata": {"customized": false, "type": "DictPort", "value": {}}, "randseed": {"customized": true, "type": "IntPort", "value": null}, "set_breakpoint": {"customized": false, "type": "BoolPort", "value": false}, "speedup": {"customized": false, "type": "FloatPort", "value": 1.0}, "start_pos": {"customized": true, "type": "FloatPort", "value": 21870.0}, "timestamp_jitter": {"customized": false, "type": "FloatPort", "value": 0.0}, "timing": {"customized": false, "type": "EnumPort", "value": "wallclock"}, "update_interval": {"customized": false, "type": "FloatPort", "value": 0.04}}, "uuid": "6b5599fc-d0f2-4017-a83f-c776a0383e04"}, "node16": {"class": "DejitterTimestamps", "module": "neuropype.nodes.utilities.DejitterTimestamps", "params": {"force_monotonic": {"customized": false, "type": "BoolPort", "value": true}, "forget_halftime": {"customized": false, "type": "FloatPort", "value": 90.0}, "max_updaterate": {"customized": false, "type": "IntPort", "value": 500}, "metadata": {"customized": false, "type": "DictPort", "value": {}}, "set_breakpoint": {"customized": false, "type": "BoolPort", "value": false}, "warmup_samples": {"customized": false, "type": "IntPort", "value": -1}}, "uuid": "40165ca7-d133-4d9a-8ab0-2bfd237bf39e"}, "node17": {"class": "SeparateStreams", "module": "neuropype.nodes.formatting.SeparateStreams", "params": {"condition": {"customized": true, "type": "ComboPort", "value": "modality=='EEG'"}, "metadata": {"customized": false, "type": "DictPort", "value": {}}, "set_breakpoint": {"customized": false, "type": "BoolPort", "value": false}}, "uuid": "7d130a6b-d6e3-411e-b1e5-fa4cb32e2778"}, "node2": {"class": "MovingWindow", "module": "neuropype.nodes.signal_processing.MovingWindow", "params": {"flag_as_offline": {"customized": false, "type": "BoolPort", "value": false}, "metadata": {"customized": false, "type": "DictPort", "value": {}}, "set_breakpoint": {"customized": false, "type": "BoolPort", "value": false}, "unit": {"customized": false, "type": "EnumPort", "value": "seconds"}, "verbose": {"customized": false, "type": "BoolPort", "value": false}, "window_length": {"customized": true, "type": "FloatPort", "value": 30.0}}, "uuid": "89924b11-481d-46e8-b8bb-8ca24d26669b"}, "node3": {"class": "PowerBands", "module": "neuropype.nodes.spectral.PowerBands", "params": {"alpha": {"customized": true, "type": "ListPort", "value": [8, 13]}, "average_across_channels": {"customized": true, "type": "BoolPort", "value": false}, "beta": {"customized": true, "type": "ListPort", "value": [13, 30]}, "correct_for_falloff": {"customized": false, "type": "BoolPort", "value": true}, "custom_bands": {"customized": false, "type": "DictPort", "value": {}}, "delta": {"customized": true, "type": "ListPort", "value": [0.5, 4]}, "gamma": {"customized": true, "type": "ListPort", "value": [30, 40]}, "keep_numeric_band_in_names": {"customized": false, "type": "BoolPort", "value": false}, "mean_trim": {"customized": false, "type": "DictPort", "value": {}}, "metadata": {"customized": false, "type": "DictPort", "value": {}}, "set_breakpoint": {"customized": false, "type": "BoolPort", "value": false}, "theta": {"customized": true, "type": "ListPort", "value": [4, 8]}, "unit": {"customized": false, "type": "EnumPort", "value": "dB"}, "verbose": {"customized": false, "type": "BoolPort", "value": true}}, "uuid": "6c13fcff-4b94-4e1f-8723-62548968bb55"}, "node4": {"class": "BarPlot", "module": "neuropype.nodes.visualization.BarPlot", "params": {"always_on_top": {"customized": false, "type": "BoolPort", "value": false}, "annotation_font_size": {"customized": false, "type": "FloatPort", "value": 11.0}, "antialiased": {"customized": false, "type": "BoolPort", "value": true}, "auto_line_colors": {"customized": false, "type": "BoolPort", "value": true}, "axis": {"customized": false, "type": "ComboPort", "value": "feature"}, "background_color": {"customized": false, "type": "StringPort", "value": "#303030"}, "colormap": {"customized": false, "type": "EnumPort", "value": "gist_rainbow"}, "decoration_color": {"customized": false, "type": "StringPort", "value": "#B0B0B0"}, "font_size": {"customized": false, "type": "FloatPort", "value": 11.0}, "initial_dims": {"customized": false, "type": "ListPort", "value": [50, 50, 1000, 800]}, "instance_field": {"customized": false, "type": "StringPort", "value": null}, "label_rotation": {"customized": false, "type": "EnumPort", "value": "horizontal"}, "left_offset": {"customized": false, "type": "IntPort", "value": 0}, "line_color": {"customized": false, "type": "StringPort", "value": "white"}, "line_width": {"customized": false, "type": "FloatPort", "value": 0.8}, "max_channels": {"customized": true, "type": "IntPort", "value": 4}, "metadata": {"customized": false, "type": "DictPort", "value": {}}, "plot_minmax": {"customized": false, "type": "BoolPort", "value": false}, "set_breakpoint": {"customized": false, "type": "BoolPort", "value": false}, "show_toolbar": {"customized": false, "type": "BoolPort", "value": false}, "stream": {"customized": false, "type": "StringPort", "value": null}, "stream_name": {"customized": false, "type": "AliasPort", "value": null}, "tight_layout": {"customized": false, "type": "BoolPort", "value": true}, "title": {"customized": true, "type": "StringPort", "value": "[21_REM, Fpz_Cz] Band Power per 30-sec Epoch"}, "track_window_position": {"customized": false, "type": "BoolPort", "value": false}, "verbose": {"customized": false, "type": "BoolPort", "value": false}, "x_label": {"customized": true, "type": "StringPort", "value": "Frequency band"}, "y_label": {"customized": true, "type": "StringPort", "value": "Power (dB)"}, "y_limits": {"customized": true, "type": "ListPort", "value": [0, 100]}, "zero_color": {"customized": false, "type": "StringPort", "value": "#606060"}}, "uuid": "d73388b9-13a1-4e8e-9e65-fcd25a6f4572"}, "node5": {"class": "FastFourierTransform", "module": "neuropype.nodes.spectral.FastFourierTransform", "params": {"axis": {"customized": false, "type": "ComboPort", "value": "time"}, "metadata": {"customized": false, "type": "DictPort", "value": {}}, "n": {"customized": false, "type": "IntPort", "value": null}, "normalization": {"customized": false, "type": "EnumPort", "value": "backward"}, "num_partitions": {"customized": false, "type": "IntPort", "value": 4}, "onesided": {"customized": true, "type": "BoolPort", "value": true}, "partition_axis": {"customized": false, "type": "ComboPort", "value": "disabled"}, "set_breakpoint": {"customized": false, "type": "BoolPort", "value": false}}, "uuid": "82712b57-fe84-4671-bd68-4deea5fc3dce"}, "node6": {"class": "Absolute", "module": "neuropype.nodes.elementwise_math.Absolute", "params": {"metadata": {"customized": false, "type": "DictPort", "value": {}}, "set_breakpoint": {"customized": false, "type": "BoolPort", "value": false}}, "uuid": "35fb123e-9074-4e8b-9821-7c9cd039befb"}, "node7": {"class": "Power", "module": "neuropype.nodes.elementwise_math.Power", "params": {"metadata": {"customized": false, "type": "DictPort", "value": {}}, "power": {"customized": true, "type": "FloatPort", "value": 2.0}, "set_breakpoint": {"customized": false, "type": "BoolPort", "value": false}}, "uuid": "9cfd9216-ddc5-4df1-92d5-0bb32d36735b"}, "node8": {"class": "SelectRange", "module": "neuropype.nodes.tensor_math.SelectRange", "params": {"apply_multiple_axes": {"customized": false, "type": "BoolPort", "value": false}, "apply_time_selection_to_markers": {"customized": false, "type": "BoolPort", "value": false}, "axis": {"customized": true, "type": "ComboPort", "value": "named"}, "drop_if_nonrange": {"customized": false, "type": "EnumPort", "value": "legacy"}, "invert_selection": {"customized": false, "type": "BoolPort", "value": false}, "metadata": {"customized": false, "type": "DictPort", "value": {}}, "selection": {"customized": true, "type": "Port", "value": ["Fpz-Cz"]}, "set_breakpoint": {"customized": false, "type": "BoolPort", "value": false}, "unit": {"customized": true, "type": "ComboPort", "value": "default"}}, "uuid": "bbc8ccea-5f2b-4254-bf69-05654191e935"}, "node9": {"class": "ImportEDF", "module": "neuropype.nodes.file_system.ImportEDF", "params": {"cloud_account": {"customized": false, "type": "StringPort", "value": ""}, "cloud_bucket": {"customized": false, "type": "StringPort", "value": ""}, "cloud_credentials": {"customized": false, "type": "StringPort", "value": ""}, "cloud_host": {"customized": false, "type": "EnumPort", "value": "Default"}, "exclude_channels": {"customized": false, "type": "ListPort", "value": []}, "filename": {"customized": true, "type": "StringPort", "value": "C:/Users/user/Desktop/SC4052EC-Hypnogram.edf"}, "metadata": {"customized": false, "type": "DictPort", "value": {}}, "set_breakpoint": {"customized": false, "type": "BoolPort", "value": false}, "stim_channel": {"customized": false, "type": "StringPort", "value": ""}, "strip_modality": {"customized": false, "type": "BoolPort", "value": true}, "unit": {"customized": false, "type": "EnumPort", "value": "uV"}}, "uuid": "c4ec497f-4d30-4a8e-978d-f347aac305ff"}}, "version": 1.1}</patch>
</scheme>
