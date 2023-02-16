from typing import NamedTuple

class FramesSection(NamedTuple):
    """
    Represents a section of frames
    """
    left: int
    right: int

    def is_mid_equal_to_limit(self):
        """
        Check if when calculating the one in the middle 
        it is equal to any of its limits.
        """
        mid = self.get_median()
        return mid in (self.left, self.right)

    def get_median(self):
        """Return median of FramesSection."""
        return (self.left + self.right) // 2

def get_partial_frame_section(
    frames_section: FramesSection, slice_toward_right: bool = True
) -> FramesSection:
    """
    Slice frames section.

    Args:
        frames_section (:class:`FramesSection`): The ``frames_section`` to slice
        slice_toward_right (:obj:`bool`): If :obj:`True` slice frames section toward right.
            If :obj:`False` slice frames section toward left.
            Defaults to :obj:`True`.
    
    Returns:
        :obj:`frames_section`: The slice frames section

    """
    left, right = frames_section
    mid = frames_section.get_median()
    if slice_toward_right:
        new_left = mid
        return FramesSection(new_left, right)
    new_right = mid
    return FramesSection(left, new_right)
