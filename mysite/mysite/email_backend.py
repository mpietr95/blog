# mysite/email_backend.py
import ssl
from django.core.mail.backends.smtp import EmailBackend as SMTPBackend

class CustomEmailBackend(SMTPBackend):
    def open(self):
        if self.connection:
            return False
        
        connection_params = {}
        if self.timeout is not None:
            connection_params['timeout'] = self.timeout
        
        try:
            if self.use_ssl:
                # SSL z wyłączoną weryfikacją certyfikatu
                self.connection = self.connection_class(
                    self.host, 
                    self.port,
                    context=ssl._create_unverified_context(),
                    **connection_params
                )
            else:
                self.connection = self.connection_class(
                    self.host, self.port, **connection_params
                )
                
                if self.use_tls:
                    self.connection.starttls(
                        context=ssl._create_unverified_context()
                    )
            
            if self.username and self.password:
                self.connection.login(self.username, self.password)
                
            return True
        except Exception:
            if not self.fail_silently:
                raise