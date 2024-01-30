class node:
    def __init__(self,data):
        self.data = data
        self.next = None

class linkedlist:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        if self.head is None:
            # If the list is empty, create a new node and set it as both head and tail
            self.head = node(data)
            self.tail = self.head
        else:
            # If the list is not empty, append a new node to the end and update  tail
            new_node = node(data)
            self.tail.next = new_node
            self.tail = new_node

    def traverse(self):
        curr = self.head
        out = ""
        while curr:
            out+=" -> " + str(curr.data)
            curr = curr.next

        print(out)
    def find_node(self, data):
        # this will find the first occurence of the node matching the argument passed in

        curr = self.head
        prev = None
        while curr.data != data:
            prev = curr
            curr= curr.next

        # returns a tuple with the previous node (for perserving linkage) and the current node
        return (prev, curr)

    def delete(self, data):
        prev, curr = self.find_node(data)

        if curr:
            if prev:
                # Node is not the head
                prev.next = curr.next
            else:
                # Node is the head
                self.head = curr.next

            if curr == self.tail:
                # Node is the tail, update the tail pointer
                self.tail = prev

            curr.next = None

    def reverse(self):
        curr = self.head
        prev = None
        next = None

        #1. save the state of the next node
        #2. set the current node to point the prev (none at first)
        #3. move prev and curr up 1 node and repeat
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next

        self.tail = self.head  # Update the tail pointer to the new head
        self.head = prev  # Update the head pointer to the last node

    def start_insert(self, data):
        if not self.head:
            self.append(data)
        else:
            temp = self.head.next
            self.head = node(data)
            self.head.next = temp

    def middle_insert(self, insertBefore, data):
        # getting previous and current node (prev, curr)
        prev, curr = self.find_node(insertBefore)

        # create a new node with the data, and insert before the target in argument
        if prev and curr:
            new_node = node(data)
            prev.next = new_node
            new_node.next = curr

    def end_insert(self, data):
        self.append(data)



# Demonstration
"A user has a music app open on their phone and wishes to queue the songs given in the list below"
"""
tracks = ["[Disturbia - Rhianna]",
          "[Notorious Thugs - Notorious B.I.G]",
          "[Miami - Will Smith]",
          "[Ma Cherie - DJ Antoine]"]

# we add them to a playlist for the user
playlist = linkedlist()

for track in tracks:
    playlist.append(track)

# Here is a printed representation of the users tracks
print("\nPlaylist: ")
playlist.traverse()


# The app has a function to reverse the order of the tracks
print("\nReversing Play Order: ")
playlist.reverse()
playlist.traverse()



# the user spontaneously selects a song to play from his library
# the app handels this by immediatly playing the selected song and setting
# the previous song to play after this one
print("\nUser Plays starts playing another song: ")
playlist.start_insert("[Boom Boom Pow - Black Eyed Peas]")
playlist.traverse()




# the user wants to queue a song a bit later in the playlist (after [Miami - Will Smith])
print("\nInserting a track in the middle of the playlist: ")
playlist.middle_insert("[Miami - Will Smith]", "[DNA - Kendrick Lamar]")
playlist.traverse()



# the user decides that he no longer wishes to listen to disturbia (for some reason)
# to remove it from the playlist, the app searches for the node representing that song
# and removes it
print("\n Removing the selected song: ")
playlist.delete("[Disturbia - Rhianna]")
playlist.traverse()



# the the app has a dedicated functionality to inserting a track to the end of the playlist
# the 'append()' function covered in class is sufficient to do this
print("\nInserting a track at the end of the playlist")
playlist.end_insert("[Hey Jude - Beatles]")
playlist.traverse()

"""