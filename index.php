<?php
include 'config.php';
//use VK\OAuth\VKOAuth;
//use VK\OAuth\VKOAuthDisplay;
//use VK\OAuth\VKOAuthResponseType;
//use VK\OAuth\Scopes\VKOAuthUserScope;
//use VK\OAuth\Scopes\VKOAuthGroupScope;

//$oauth = new VKOAuth();
//$display = VKOAuthDisplay::PAGE;
//$scope = array(VKOAuthGroupScope::WALL);
//$state = 'secret_state_code';

//$browser_url = $oauth->getAuthorizeUrl(VKOAuthResponseType::CODE, ID, URL, $display, $scope, $state, ID_GROUP);


?>
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title> Crossposting </title>
</head>
<body>
<!-- <form method="post" action="linker.php"> -->
<!-- <a href="https://oauth.vk.com/authorize?client_id=<?=ID?>&display=page&redirect_uri=http://api.vk.com/blank.html&scope=wall,offline,groups,manage&response_type=code"
       target="_blank">   <img src="vk.png" width="50" height="50" alt="VK">    </a> -->

<!-- <a href="https://oauth.vk.com/authorize?client_id=<?=ID?>&display=page&redirect_uri=<?=URL?>&scope=wall,offline,groups,manage&response_type=code"
         target="_blank">   <img src="vk2.png" width="50" height="50" alt="VK2">    </a> -->

        <a href="https://oauth.vk.com/authorize?client_id=<?=ID?>&display=page&redirect_uri=http://api.vk.com/blank.html&&scope=wall,offline,groups,manage&response_type=token&v=5.101"
       target="_blank">   <img src="vk.png" width="50" height="50" alt="VK">    </a>

     <a href="https://oauth.vk.com/authorize?client_id=<?=ID?>&display=page&redirect_uri=<?=URL?>&scope=wall,offline,groups,manage&response_type=code&v=5.101"
        target="_blank">   <img src="vk2.png" width="50" height="50" alt="VK2">    </a>

        <!-- </form> -->
</body>
</html>

<?php

//group_ids=<?=ID_GROUP? >
require 'C:\Users\Homiak\Documents\MDKP\testPHP2\vendor\autoload.php';
//client
use VK\Client\VKApiClient;
use VK\Client\VKApiError;
use VK\Client\VKApiRequest;
use VK\Client\Enums\VKLanguage;
//exceptions
use VK\Exceptions\VKApiException;
use VK\Exceptions\VKClientExceptionException;
use VK\Exceptions\VKOAuthExceptionExceptionException;
//exceptions api +100500
//OAuth
//use VK\OAuth\VKOAuth;
//use VK\OAuth\VKOAuthDisplay;
//use VK\OAuth\VKOAuthResponseType;
//use VK\OAuth\Scopes\VKOAuthUserScope;
//use VK\OAuth\Scopes\VKOAuthGroupScope;
//transport client
use VK\OAuth\TransportClient;
use VK\OAuth\TransportClientResponce;
use VK\OAuth\TransportClientExceptions;
use VK\OAuth\Curl\CurlHttpClient;

?>






<?php

?>