<?php

include 'config.php';
//------------------------
//$vk = new VKApiClient();

//------------------------

if(!$_GET['code']) {
    exit('error code');
}

// получаем токен
//$code1 = "0db0d6e648a3383cd8";
//$token = "9549f9468d12b45baeba4c8c161290022d61dc2921c3fb4669e9783637839384b0d78d856cf8577152c3f"; //json_decode(file_get_contents('https://oauth.vk.com/access_token?client_id='.ID.'&redirect_uri='.URL.'&client_secret='.SECRET.'&code='.$code1), true); //.$_GET['code']), true);

//if(!$token) {
//    exit('error token');
//}

echo '<pre>';
//var_dump($token);
echo '</pre>';


//получаем данные
//$data = json_decode(file_get_contents('https://api.vk.com/method/users.get?user_id='.$token['user_id'].'&access_token='.$token['access_token'].'&v=5.101&fields=uid,first_name,last_name,photo_small,sex'), true);

//if(!$data) {
//    exit('error data');
//}

echo '<pre>';
//var_dump($data);
echo '</pre>';


// ----------- моё творчество ----------------



$token = "3ad6f91ddb3def9649d44c45a5f2f1532f12439b885161496b32523659f614c44b79aa4cdf7adf0fda1f5"; //json_decode(file_get_contents('https://oauth.vk.com/access_token?client_id='.ID.'&redirect_uri='.URL.'&client_secret='.SECRET.'&code='.$code1), true); //.$_GET['code']), true);
$text = 'POST_VK_test';
/* $post = json_decode(file_get_contents('https://api.vk.com/method/wall.post?owner_id=-'.$group_id.'&access_token='.$token['access_token'].'&v=5.101&from_group=1&message='.$text),true);
$post = json_decode(file_get_contents('https://api.vk.com/method/groups.isMember?group_id='.ID_GROUP.'&v=5.101&user_id=104166508&extended=1&access_token='.$token['access_token']),true);

if(!$post) {
    exit('error post');
}

echo '<pre>';
var_dump($post);
echo '</pre>'; */

//['access_token']
$post = json_decode(file_get_contents('https://api.vk.com/method/wall.post?owner_id=-'.ID_GROUP.'&access_token='.$token.'&v=5.101&from_group=1&message='.$text),true);
if(!$post) {
    exit('error post');
}

echo '<pre>';
var_dump($post);
echo '</pre>';









//$group_id = "-127630582";
//$text = 'POST_VK';
//$post = json_decode(file_get_contents('https://api.vk.com/method/wall.post?owner_id='.$group_id.'&access_token='.$token['access_token'].'&v=5.101&from_group=1&message='.$text),true);

//if(!$post) {
//    exit('error post');
//}

//echo '<pre>';
//var_dump($post);
//echo '</pre>';

?>


