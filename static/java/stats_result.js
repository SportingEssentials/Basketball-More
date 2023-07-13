
function copyToClipboard(text) {
  navigator.clipboard.writeText(text)
    .then(() => {
      alert('Link copied to clipboard!');
    })
    .catch((error) => {
      console.error('Failed to copy text: ', error);
    });
}




