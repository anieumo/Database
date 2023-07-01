# Database
This is a front-end model for a Database is a way to handle clean visualization of shot and asset creation.

It contains the shots, sequences, and asset list of a fake short, organized in an easily concepted way. Right-clicking
on a shot or asset opens a context menu that lets the user add a shot, sequence, new asset version, or new asset. The database is a QModel of an Asset folder for a short film. 

To create a new sequence, right click on the app and "Create New Sequence". Sequences are indicated by a camera icon and named witha three letter sequence in thebinput field. Once a new sequence is created, right click on that and "Create a New Shot" with a 4 number sequence. Beneath that field, one may add an asset type of either a mesh("mesh.main"), a texture("mesh.maps"), or a previz shot("previz"). Each upload of an asset type is handled by a "version". Each version is indicated by a stack of books. To add a new version right click on the latest version and "Create New Version"
