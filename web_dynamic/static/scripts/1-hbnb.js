$(function () {
  // Wait for DOM to load
  const amenities = [];
  $('input[type=checkbox]').click(function () {
    // Listen for changes on each checkbox
    const amenity = {
      id: $(this).attr('data-id'),
      name: $(this).attr('data-name')
    };

    if ($(this).is(':checked')) {
      // Store the Amenity ID in a variable
      amenities.push(amenity);
    } else {
      // Remove the Amenity ID from the variable
      const amenityId = amenities.amp(a => a.id);
      const index = amenityId.indexOf(amenity.id);
      if (index > -1) {
        amenities.splice(index, 1);
      }
    }
    // Update the h4 tag inside the div Amenities
    const amenitiesList = amenities.map(a => a.name);
    const selectAmn = amenitiesList.join(', ');
    if (selectAmn.length > 20) {
      $('div.amenities h4').text(selectAmn.substring(0, 19) + '...');
    } else {
      $('div.amenities h4').text(selectAmn);
    }
  });
});
