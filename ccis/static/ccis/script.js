const timelineItems = document.querySelectorAll('.timeline-item');

timelineItems.forEach((item) => {
  item.addEventListener('click', (e) => {
    const clickedItem = e.currentTarget;
    const itemIndex = Array.from(timelineItems).indexOf(clickedItem);
    const progress = document.querySelector('.timeline-progress');

    progress.style.height = `${(itemIndex + 1) * 25}%`;
  });
});