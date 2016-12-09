var myContent = {
  pictureList : [
  "url(http://www.irishtimes.com/polopoly_fs/1.2280664.1436543517!/image/image.jpg_gen/derivatives/box_620_330/image.jpg)",
  "url(http://i.dailymail.co.uk/i/pix/2015/12/29/19/2FAB3E6100000578-3377927-Andrew_Suryono_Bali_I_was_taking_pictures_of_some_Orangutans_in_-a-42_1451416773881.jpg)",
  "url(http://www.popsci.com/sites/popsci.com/files/styles/large_1x_/public/images/2016/05/hubbleheader.png?itok=BSsBG9gD&fc=50,50)",
  "url(http://www.telegraph.co.uk/content/dam/news/2016/05/17/98223710_marmoset-large_trans++eo_i_u9APj8RuoebjoAHt0k9u7HhRJvuo-ZLenGRumA.jpg)",
  "url(http://www.telegraph.co.uk/content/dam/news/2016/10/06/110549255_DUNSTABLE%20UNITED%20KINGDOM%20-%20OCTOBER%2006%20Close%20up%20shots%20of%20the%20reticulated%20giraffe%20at%20ZSL%20Whi-large_trans++wRnwQ0KgCqCTKamrqQKaYn-5rYAcEMfZ-k6qzXXxMMM.jpg)"],

  headings : ["Kite-flying", "Monkey with an umbrella", "The beautiful Universe", "Little monkeys", "Giraffe Love"],

  paragraphs : ["Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.",
                "Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam, eaque ipsa quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt explicabo. Nemo enim ipsam voluptatem quia voluptas sit aspernatur aut odit aut fugit.",
                "Sit amet, consectetur, adipisci velit, sed quia non numquam eius modi tempora incidunt ut labore et dolore magnam aliquam quaerat voluptatem. Ut enim ad minima veniam, quis nostrum exercitationem ullam corporis suscipit laboriosam, nisi ut aliquid ex ea commodi consequatur.",
                "At vero eos et accusamus et iusto odio dignissimos ducimus qui blanditiis praesentium voluptatum deleniti atque corrupti quos dolores et quas molestias excepturi sint occaecati cupiditate non provident, similique sunt in culpa qui officia deserunt mollitia animi, id est laborum et dolorum fuga.",
                "Et harum quidem rerum facilis est et expedita distinctio. Nam libero tempore, cum soluta nobis est eligendi optio cumque nihil impedit quo minus id quod maxime placeat facere possimus, omnis voluptas assumenda est, omnis dolor repellendus. Temporibus autem quibusdam et aut officiis."]
  };

var myPicture = document.querySelector(".main");
var nextButton = document.querySelector(".next");
var prevButton = document.querySelector(".prev");
var picListLength = myContent.pictureList.length;
var currentPosition = 0;
var myHeading = document.querySelector("h1");
var myParagraph = document.querySelector('p')

function disableButton() {
  if (currentPosition === 0) {
    prevButton.setAttribute("disabled", "true");
    prevButton.setAttribute("id", "not_working")

  } else {
    prevButton.removeAttribute("disabled");
    prevButton.removeAttribute("id");

  }

  if (currentPosition === picListLength -1) {
    nextButton.setAttribute("disabled", "true");
    nextButton.setAttribute("id", "not_working")
  } else {
    nextButton.removeAttribute("disabled");
    nextButton.removeAttribute("id");
  }
}

function changePic(){
  nextButton.addEventListener("click", function(e){
    if (currentPosition < picListLength -1) {
      currentPosition += 1;
      console.log(currentPosition);
      console.log(nextButton);
      myPicture.style.backgroundImage = myContent.pictureList[currentPosition];
      myHeading.innerHTML = myContent.headings[currentPosition];
      myParagraph.innerHTML = myContent.paragraphs[currentPosition];
      disableButton();
    }
  });
  prevButton.addEventListener("click", function(e){
    if (currentPosition > 0) {
      console.log(currentPosition);
      currentPosition -= 1;
      myPicture.style.backgroundImage = myContent.pictureList[currentPosition];
      myHeading.innerHTML = myContent.headings[currentPosition];
      myParagraph.innerHTML = myContent.paragraphs[currentPosition];
      disableButton();
    }
  });
}
changePic();
