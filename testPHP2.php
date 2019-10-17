<?php

//echo "Hello world";
//require __DIR__ . '/../vendor/autoload.php';C:\Users\Homiak\Documents\MDKP\testPHP2\vendor
require 'C:\Users\Homiak\Documents\MDKP\testPHP2\vendor\autoload.php';

//app id 529762531091184
//user id 113831840020697
//secret eaeb788f99bfc49e6eebac9b30d2143f
//access_token": "529762531091184|wiKY8kxQfdgt03i-Puufm5_Xy8U"
//oauth/access_token?grant_type=fb_exchange_token&client_id=	529762531091184&client_secret=eaeb788f99bfc49e6eebac9b30d2143f&fb_exchange_token=

$app_id = '529762531091184'; // ид приложения. берешь в настройках приложения (или копируешь с адресной строки)
$app_secret = 'eaeb788f99bfc49e6eebac9b30d2143f'; // ключ приложения. берешь в настройках приложения
$access_token = 'EAAHh0PN7IvABALXsqkDN6pIjjwrbm7P6lAMmUW5ZByFfD62QzXpldhHo0BtHtdxAHv7lfOAbcfwf0BqGirEb7qcznD9ii0aF3nSZBVqWuHgE2WHUmXujRuG8hWLC54GznYETj77v3HZCz1mZALyK9ZC6dHDNGpJb6tY8XY1oguwj7N3QzpDQk'; // токен, который мы получили
$page_id = '985618928451302'; // id группы 985618928451302 ( id страницы 100041816445446)


//use  Facebook\Facebook;

$fb = new Facebook\Facebook(array(
    'app_id' => $app_id,
    'app_secret' => $app_secret,
    'default_graph_version' => 'v2.2',
));

/*/////////////////////////////////////////////////////////////////////
$helper = $fb->getRedirectLoginHelper();

//Добавьте разрешение publish_actions, чтобы постить от имени пользователя, а не от имени страницы
$permissions = ['manage_pages','publish_pages'];

$loginUrl = $helper->getLoginUrl('https://www.facebook.com/', $permissions);
$helper = $fb->getRedirectLoginHelper();

try {

    $accessToken = $helper->getAccessToken();

}

catch(Facebook\Exceptions\FacebookResponseException $e) {

    echo 'Graph вернул ошибку: ' . $e->getMessage();
    exit;

}

catch(Facebook\Exceptions\FacebookSDKException $e) {

    echo 'Facebook SDK вернул ошибку: ' . $e->getMessage();
    exit;

}

if (isset($accessToken))
    $_SESSION['EAAHh0PN7IvABALXsqkDN6pIjjwrbm7P6lAMmUW5ZByFfD62QzXpldhHo0BtHtdxAHv7lfOAbcfwf0BqGirEb7qcznD9ii0aF3nSZBVqWuHgE2WHUmXujRuG8hWLC54GznYETj77v3HZCz1mZALyK9ZC6dHDNGpJb6tY8XY1oguwj7N3QzpDQk'] = (string) $accessToken;

elseif ($helper->getError())
    exit;

try {

    $response = $fb->get('/denis.baryshev.52?fields=access_token', $_SESSION['EAAHh0PN7IvABALXsqkDN6pIjjwrbm7P6lAMmUW5ZByFfD62QzXpldhHo0BtHtdxAHv7lfOAbcfwf0BqGirEb7qcznD9ii0aF3nSZBVqWuHgE2WHUmXujRuG8hWLC54GznYETj77v3HZCz1mZALyK9ZC6dHDNGpJb6tY8XY1oguwj7N3QzpDQk']);

}

catch (Facebook\Exceptions\FacebookResponseException $e) {

    echo 'Graph вернул ошибку: ' . $e->getMessage();
    exit;

}

catch (Facebook\Exceptions\FacebookSDKException $e) {

    echo 'Facebook SDK вернул ошибку: ' . $e->getMessage();
    exit;

}

//Токен страницы
echo $response->getGraphNode()['EAAHh0PN7IvABALXsqkDN6pIjjwrbm7P6lAMmUW5ZByFfD62QzXpldhHo0BtHtdxAHv7lfOAbcfwf0BqGirEb7qcznD9ii0aF3nSZBVqWuHgE2WHUmXujRuG8hWLC54GznYETj77v3HZCz1mZALyK9ZC6dHDNGpJb6tY8XY1oguwj7N3QzpDQk'];
*///////////////////////////////////////////////////////////////
$fb->setDefaultAccessToken($access_token);

// а тут мы непосредственно постим запись на стену.
// в этом примере запись представляет собой картинку + текст
$data = [
    'message' => 'Текст',
    'source' => $fb->fileToUpload('C:\Users\Homiak\Desktop\Exxx4vQRmnI.jpg'),
];
$batch = [
    'photo' => $fb->request('POST', "/{$page_id}/photos", $data),
];
$responses = $fb->sendBatchRequest($batch);

//// 2 вариант
/*$fbApi = new Facebook/Facebook([
    'app_id' => $app_id,
    'app_secret' => $app_secret
    //'default_graph_version' => 'v2.2',
]);
$post = [
    'message' => 'текст сообщения',
];
$accessToken = new Facebook\Authentication\AccessToken($access_token);
$fb->post(
    $page_id,
    $post,
    $accessToken
);*/

///////////////////////////////////////////////////////// VK API
/*use VK\Client\VKApiClient;
use VK\Client\Enums\VKLanguage;
use VK\OAuth\VKOAuth;
use VK\OAuth\VKOAuthDisplay;
use VK\OAuth\VKOAuthResponseType;
use VK\OAuth\Scopes\VKOAuthUserScope;
use VK\OAuth\Scopes\VKOAuthGroupScope;

//$vk = new \VK\Client\VKApiClient();
$vk = new VKApiClient();
//$vk = new VKApiClient('5.95');
//$vk = new VKApiClient('5.95', VKLanguage::ENGLISH);

$oauth = new VKOAuth();
$client_id = 1234567;
$redirect_uri = 'https://example.com/vk';
$display = VKOAuthDisplay::PAGE;
$scope = array(VKOAuthUserScope::WALL, VKOAuthUserScope::GROUPS);
$state = 'secret_state_code';

$browser_url = $oauth->getAuthorizeUrl(VKOAuthResponseType::CODE, $client_id, $redirect_uri, $display, $scope, $state);

$oauth = new VKOAuth();
$client_id = 1234567;
$client_secret = 'SDAScasd';
$redirect_uri = 'https://example.com/vk';
$code = 'CODE';

$response = $oauth->getAccessToken($client_id, $client_secret, $redirect_uri, $code);*/
//$access_token = $response['access_token'];


/////////////////////////////////////////////////////////////////////// Instagram
/*set_time_limit(0);
date_default_timezone_set('UTC');

require __DIR__ . '/../vendor/autoload.php';

/////// CONFIG ///////
$username = '';
$password = '';
$debug = true;
$truncatedDebug = false;
//////////////////////

/////// MEDIA ////////
$photoFilename = '';
$captionText = '';
//////////////////////

$ig = new \InstagramAPI\Instagram($debug, $truncatedDebug);

try {
    $ig->login($username, $password);
} catch (\Exception $e) {
    echo 'Something went wrong: ' . $e->getMessage() . "\n";
    exit(0);
}

try {
    // The most basic upload command, if you're sure that your photo file is
    // valid on Instagram (that it fits all requirements), is the following:
    // $ig->timeline->uploadPhoto($photoFilename, ['caption' => $captionText]);

    // However, if you want to guarantee that the file is valid (correct format,
    // width, height and aspect ratio), then you can run it through our
    // automatic photo processing class. It is pretty fast, and only does any
    // work when the input file is invalid, so you may want to always use it.
    // You have nothing to worry about, since the class uses temporary files if
    // the input needs processing, and it never overwrites your original file.
    //
    // Also note that it has lots of options, so read its class documentation!
    $photo = new \InstagramAPI\Media\Photo\InstagramPhoto($photoFilename);
    $ig->timeline->uploadPhoto($photo->getFile(), ['caption' => $captionText]);
} catch (\Exception $e) {
    echo 'Something went wrong: ' . $e->getMessage() . "\n";
}*/