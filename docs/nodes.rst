Working with Nodes
===================

Nodes are the core abstraction in KelDB.

What is a Node?
---------------

The Node object represents a singular node in the tree.

Example:

.. code-block:: text

   /
   ├── users/
   │   ├── alice/
   │   └── bob/
   └── config/

Creating Nodes
--------------

Nodes are created dynamically:

.. code-block:: python

   users = await db.get_subnode("users") # Nothing is created yet
   alice = await users.get_subnode("alice") # Still nothing
   await alice.set_value(None) # Now the nodes are created recursively

Setting Values
--------------

Nodes can store any JSON-serializable value:

.. code-block:: python

   await alice.set_value({
       "age": 25,
       "active": True
   })

All values are saved automatically, there is no save mechanism.

Reading Values
--------------

.. code-block:: python

   data = await alice.get_value()
   print(data)

Listing Subnodes
----------------

.. code-block:: python

   async for child in users.list_subnodes():
       print(child.name)

Deleting Nodes
--------------

.. code-block:: python

   await alice.delete()