const offer_extra_image_button1 = document.querySelector(".offer_extra_image_button1");
const offer_extra_image_button2 = document.querySelector(".offer_extra_image_button2");
const offer_extra_image_button3 = document.querySelector(".offer_extra_image_button3");

offer_extra_image_button1.addEventListener("click", () => {
    document.querySelector(".extra_image_id1").value = 1;
});

offer_extra_image_button2.addEventListener("click", () => {
    document.querySelector(".extra_image_id2").value = 2;
});

offer_extra_image_button3.addEventListener("click", () => {
    document.querySelector(".extra_image_id3").value = 3;
});

function mainImageDelete(offer_id) {
    document.querySelector(".main_image_id").value = offer_id;
}

function offerVideoDelete(video_id) {
    document.querySelector(".offer_video_id").value = video_id;
}

function offerDocumentDelete(doc_id) {
    document.querySelector(".offer_document_id").value = doc_id;
}